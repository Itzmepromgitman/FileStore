import asyncio
import re
from datetime import datetime, timedelta

from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message

from config import LOGGER
from database.database import get_variable, set_variable

log = LOGGER(__name__)


def parse_duration(duration_str):
    """
    Parses a duration string like '1d 2h 30m 45s' or '5d' and returns a timedelta.
    """
    matches = re.findall(r"(\d+)\s*([dhms])", duration_str.lower())
    if not matches:
        raise ValueError("Invalid duration format")
    delta = timedelta()
    for value, unit in matches:
        value = int(value)
        if unit == "d":
            delta += timedelta(days=value)
        elif unit == "h":
            delta += timedelta(hours=value)
        elif unit == "m":
            delta += timedelta(minutes=value)
        elif unit == "s":
            delta += timedelta(seconds=value)
    return delta


async def add_premium(client, message: Message):
    args = message.text.split(maxsplit=2)
    user_id = None
    time_text = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if len(args) > 1:
            time_text = args[1]
    elif len(args) == 3:
        user_id = args[1]
        time_text = args[2]

    if not user_id:
        await message.reply(
            "❓ Please reply to a user or use `/add_prem<user_id> <time>`.",
            quote=True,
        )
        return

    while not time_text:
        ask_msg = await message.reply(
            "💎 <b>Set Premium Duration</b>\n\n"
            "🕒 <b>Examples:</b> <code>1d</code> <code>2h</code> <code>30m</code> <code>45s</code>\n"
            "🔤 <b>Format:</b> <code>[number][d/h/m/s]</code>\n"
            "  <b>d</b> = days <b>h</b> = hours <b>m</b> = minutes <b>s</b> = seconds\n\n"
            "❌ <b>Type</b> <code>cancel</code> to abort.",
            quote=True,
        )
        try:
            resp = await client.listen(
                chat_id=message.chat.id, user_id=message.from_user.id, timeout=30
            )
        except Exception:
            await ask_msg.edit(
                "⌛ <b>Timeout!</b> Operation <b>cancelled</b>.\n\n🔁 Please try again."
            )
            return
        if resp.text.lower() in ["cancel", "❌"]:
            await ask_msg.edit("❌ Cancelled.")
            return
        time_text = resp.text.strip()

    try:
        expires_in = parse_duration(time_text)
    except ValueError:
        await message.reply(
            "⚠️ <b>Invalid time format!</b>\n"
            "📝 <b>Examples:</b> <code>1d</code> <code>2h 30m</code> <code>1d 5m 25s</code>\n"
            "  <b>d</b> = days <b>h</b> = hours <b>m</b> = minutes <b>s</b> = seconds",
            quote=True,
        )
        return

    if expires_in.total_seconds() == 0:
        await message.reply(
            "⚠️ <b>Duration must be greater than zero!</b>",
            quote=True,
        )
        return

    expires_at = datetime.now() + expires_in
    expires_iso = expires_at.isoformat()

    pusers = await get_variable("puser") or {}
    existed = str(user_id) in pusers

    pusers[str(user_id)] = expires_iso
    await set_variable("puser", pusers)

    action = "🔁 Updated" if existed else "✅ Added"
    await message.reply(
        f"{action} premium for `{user_id}` until `{expires_at.strftime('%Y-%m-%d %H:%M:%S')}`",
        quote=True,
    )


async def remove_premium(client, message: Message):
    args = message.text.split(maxsplit=1)
    user_id = None

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(args) == 2:
        user_id = args[1]
    else:
        await message.reply(
            "❓ Please reply to a user or use `/rempremium <user_id>`.", quote=True
        )
        return

    pusers = await get_variable("puser") or {}

    if str(user_id) not in pusers:
        await message.reply("⚠️ This user is not in the premium list.", quote=True)
        return

    pusers.pop(str(user_id))
    await set_variable("puser", pusers)

    await message.reply(f"❌ Removed premium access for `{user_id}`", quote=True)


async def check_and_clean_premium_users():
    while True:
        try:
            pusers = await get_variable("puser") or {}
            updated_pusers = {}

            now = datetime.now()
            for user_id, exp_date_str in pusers.items():
                try:
                    exp_date = datetime.fromisoformat(exp_date_str)
                    if exp_date > now:
                        updated_pusers[user_id] = exp_date_str
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")
                    continue

            if updated_pusers != pusers:
                await set_variable("puser", updated_pusers)

        except Exception as e:
            print(f"Error in premium check loop: {e}")

        await asyncio.sleep(600)


async def list_premium_users(client, message: Message):
    pusers = await get_variable("puser") or {}

    if not pusers:
        await message.reply("❌ No premium users found.", quote=True)
        return

    now = datetime.now()
    lines = []
    count = 1

    for uid, exp_str in pusers.items():
        try:
            exp_time = datetime.fromisoformat(exp_str)
            remaining = exp_time - now

            if remaining.total_seconds() <= 0:
                continue

            if remaining.days > 0:
                time_left = f"{remaining.days}d {remaining.seconds // 3600}h"
            elif remaining.seconds > 3600:
                time_left = (
                    f"{remaining.seconds // 3600}h {(remaining.seconds % 3600) // 60}m"
                )
            elif remaining.seconds > 60:
                time_left = f"{remaining.seconds // 60}m"
            else:
                time_left = f"{remaining.seconds}s"

            try:
                user = await client.get_users(uid)
                user_mention = f"<a href='tg://user?id={uid}'>👤 {user.first_name}</a>"
            except PeerIdInvalid:
                user_mention = "❓ Unknown User"

            lines.append(
                f"{count}. {user_mention} | 🆔 <code>{uid}</code>\n"
                f"    ⏳ Expires: <code>{exp_time.strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
                f"    🕒 Time Left: <b>{time_left}</b>"
            )
            count += 1

        except Exception as e:
            print(f"Error parsing {uid}: {e}")
            continue

    if not lines:
        await message.reply("❌ No valid premium users found.", quote=True)
        return

    text = "💎 <b>Premium Users List</b> 💎\n\n" + "\n\n".join(lines)
    await message.reply(text, quote=True, disable_web_page_preview=True)
