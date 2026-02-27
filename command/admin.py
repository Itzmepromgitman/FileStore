import re
from urllib.parse import urlparse

from pyrogram.errors.pyromod.listener_timeout import ListenerTimeout
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from database.database import get_variable, set_variable


async def admin(client, message):
    a = await get_variable("admin", [])
    txt = f"<blockquote expandable>💠 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋  ♻️\n</blockquote>\n<blockquote expandable>🚩 𝐀𝐃𝐌𝐈𝐍 :- {a}\n</blockquote>\n<blockquote expandable>⚠️ 𝐍𝐎𝐓𝐄 - ADMINS CAN USE ALL BOT COMMMANDS EXCEPT FSUB, ADMIN ‼️</blockquote>"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐀𝐃𝐃 𝐀𝐃𝐌𝐈𝐍", callback_data="admin_add"),
                InlineKeyboardButton("𝐑𝐄𝐌𝐎𝐕𝐄 𝐀𝐃𝐌𝐈𝐍", callback_data="admin_rem"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await message.reply_photo(
        photo="https://i.ibb.co/kVwykh4J/ce566244dba9.jpg",
        caption=txt,
        reply_markup=keyboard,
        message_effect_id=5104841245755180586,
    )


async def admin2(client, query):
    uid = query.from_user.id
    user_id = uid
    admin1 = await get_variable("owner", "5426061889")
    admin1 = [int(x.strip()) for x in admin1.split()]
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1]

    if uid not in admin1:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    txt = (
        "<blockquote expandable>⚠️ <b>𝖣𝗈 𝖮𝗇𝖾 𝖡𝖾𝗅𝗈𝗐</b> ⚠️</blockquote>\n"
        "<blockquote expandable><i>🔱 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗋𝗈𝗆 𝖠𝖽𝗆𝗂𝗇</i></blockquote>\n"
        "<blockquote expandable><i>💠 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝖽𝗆𝗂𝗇 𝖨𝖣</i></blockquote>"
        "<blockquote>♨️ 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗔𝗗𝗠𝗜𝗡 𝗜𝗗 𝗜𝗦 𝗩𝗔𝗟𝗜𝗗 ♨️</blockquote>"
    )

    if action == "add":
        while True:
            b = await client.send_message(
                uid,
                text=txt,
                reply_markup=ReplyKeyboardMarkup(
                    [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                ),
            )
            try:
                a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
            except ListenerTimeout:
                await client.send_message(
                    chat_id=uid,
                    text="⏳ Timeout! Fsub Setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break
            if a.forward_from_chat:
                chat_id = a.forward_from_chat.id
            else:
                if a.text.lower() == "❌ cancel":
                    await client.send_message(
                        chat_id=uid,
                        text="❌ Fsub setup cancelled.",
                        reply_markup=ReplyKeyboardRemove(),
                    )
                    await b.delete()
                    break
                try:
                    chat_id = int(a.text.strip())
                except ValueError:
                    await client.send_message(
                        user_id, "Invalid input! Please send a valid channel/group ID."
                    )
                    await b.delete()
                    continue
            admin1 = await get_variable("admin", [])

            if chat_id in admin1:
                await client.send_message(
                    user_id, "User is already admin resend correct id...."
                )
                await b.delete()
                continue
            admin1.append(chat_id)

            # Convert back to string format

            await set_variable("admin", admin1)
            await b.delete()
            await admin(client, query.message)
            await query.message.delete()
            break

    elif action == "rem":
        while True:
            b = await client.send_message(
                uid,
                text=txt,
                reply_markup=ReplyKeyboardMarkup(
                    [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                ),
            )
            try:
                a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
            except ListenerTimeout:
                await client.send_message(
                    chat_id=uid,
                    text="⏳ Timeout! Fsub Setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break
            if a.forward_from_chat:
                chat_id = a.forward_from_chat.id
            else:
                if a.text.lower() == "❌ cancel":
                    await client.send_message(
                        chat_id=uid,
                        text="❌ Fsub setup cancelled.",
                        reply_markup=ReplyKeyboardRemove(),
                    )
                    await b.delete()
                    break
                try:
                    chat_id = int(a.text.strip())
                except ValueError:
                    await client.send_message(
                        user_id, "Invalid input! Please send a valid channel/group ID."
                    )
                    await b.delete()
                    continue
            admin1 = await get_variable("admin", [])

            if chat_id not in admin1:
                await client.send_message(
                    user_id, "User is not admin resend correct id...."
                )
                await b.delete()
                continue
            admin1.remove(chat_id)

            # Convert back to string format
            await set_variable("admin", admin1)
            await b.delete()
            await admin(client, query.message)
            await query.message.delete()
            break

    else:
        # Handle unexpected action (optional)
        await query.answer("Invalid action.", show_alert=True)


async def short(client, message):
    a = await get_variable("api", "None")
    c = await get_variable("bypass", "0")
    b = await get_variable("website", "None")
    aba = await get_variable("short", "")
    mode = await get_variable("mode", "I")
    if aba and mode == "24":
        d = "𝟐𝟒𝐇 ✅"
        e = "✅"
        f = ""
    elif aba and mode == "link":
        d = "𝐏𝐄𝐑 𝐋𝐈𝐍𝐊 ✅"
        f = "✅"
        e = ""
    elif not aba:
        d = "❌"
        e = ""
        f = ""
    else:
        d = ""
        e = ""
        f = ""
    g = await get_variable("token_time", 0)

    total_seconds = int(g)  # Convert to integer

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    time_parts = []
    if hours:
        time_parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes:
        time_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds and not hours:  # Only show seconds if there are no hours
        time_parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    g = " ".join(time_parts) if time_parts else "0 seconds"

    txt = f"<blockquote expandable>♻️ 𝐒𝐇𝐎𝐑𝐓𝐍𝐄𝐑 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 💠</blockquote>\n<blockquote>💥 𝐒𝐇𝐎𝐑𝐓𝐍𝐄𝐑 𝐌𝐎𝐃𝐄: {d} </blockquote>\n<blockquote>⭐ 𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐓𝐈𝐌𝐄 : {g} </blockquote>\n<blockquote expandable>⚠️ 𝐀𝐏𝐈 : {a}</blockquote>\n<blockquote expandable>🌐 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 : {b}</blockquote>\n<blockquote expandable>𝐋𝐈𝐍𝐊𝐒 𝐁𝐘𝐏𝐀𝐒𝐒𝐄𝐃 : {c}</blockquote>"

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("𝐑𝐄𝐌𝐎𝐕𝐄 𝐒𝐇𝐎𝐑𝐓𝐄𝐑 ❌", callback_data="short_rem")],
            [
                InlineKeyboardButton(f"𝟐𝟒𝐇 𝐌𝐎𝐃𝐄 {e}", callback_data="mode_24"),
                InlineKeyboardButton(f"𝐏𝐄𝐑 𝐋𝐈𝐍𝐊 𝐌𝐎𝐃𝐄 {f}", callback_data="mode_link"),
            ],
            [
                InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐆𝐄 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 ", callback_data="short_web"),
                InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐆𝐄 𝐀𝐏𝐈", callback_data="short_api"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    await message.reply_photo(
        photo="https://i.ibb.co/5xtpFb2T/f4faad6ca1c1.jpg",
        caption=txt,
        reply_markup=keyboard,
        message_effect_id=5104841245755180586,
    )


async def short2(client, query):
    uid = query.from_user.id
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    # Extract "on" or "off" from the callback data
    await get_variable("website", "")
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    action = query.data.split("_")[1]
    txt = "<blockquote expandable>𝐏𝐋𝐄𝐀𝐒𝐄 𝐒𝐄𝐍𝐃 𝐌𝐄 𝐒𝐇𝐎𝐑𝐓𝐍𝐄𝐑 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 </blockquote>"
    tot = "<blockquote expandable>𝐏𝐋𝐄𝐀𝐒𝐄 𝐒𝐄𝐍𝐃 𝐌𝐄 𝐒𝐇𝐎𝐑𝐓𝐍𝐄𝐑 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 𝐀𝐏𝐈</blockquote>"
    if action == "web":
        while True:
            b = await client.send_message(
                uid,
                text=txt,
                reply_markup=ReplyKeyboardMarkup(
                    [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                ),
            )
            try:
                a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
            except ListenerTimeout:
                await client.send_message(
                    chat_id=uid,
                    text="⏳ Timeout! Fsub Setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break
            if a.text.lower() == "❌ cancel":
                await client.send_message(
                    chat_id=uid,
                    text="❌  WEBSITE setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break

            try:
                parsed_url = urlparse(a.text)
            except BaseException:
                await client.send_message(
                    chat_id=uid,
                    text="Please send me full website link like https://enxample.com",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                continue

            if (
                parsed_url.scheme == "https"
                and parsed_url.netloc
                and not parsed_url.path.strip("/")
            ):
                pass
            else:
                await client.send_message(
                    chat_id=uid,
                    text="Please send me full website link like https://enxample.com",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                continue

            await set_variable("website", a.text)
            await client.send_message(
                chat_id=uid, text="✅ 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 𝐀𝐃𝐃𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 "
            )
            await b.delete()
            await short(client, query.message)
            await query.message.delete()
            break
    if action == "api":
        while True:
            b = await client.send_message(
                uid,
                text=tot,
                reply_markup=ReplyKeyboardMarkup(
                    [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                ),
            )
            try:
                a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
            except ListenerTimeout:
                await client.send_message(
                    chat_id=uid,
                    text="⏳ Timeout! Fsub Setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break
            if a.text.lower() == "❌ cancel":
                await client.send_message(
                    chat_id=uid,
                    text="❌  WEBSITE setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await b.delete()
                break
            await set_variable("api", a.text)
            await client.send_message(chat_id=uid, text="✅  𝐀𝐏𝐈 𝐀𝐃𝐃𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 ")
            await b.delete()
            await short(client, query.message)
            await query.message.delete()
            break


async def short3(client, query):
    uid = query.from_user.id
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    # Extract "on" or "off" from the callback data
    await get_variable("website", "")
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    aba = await get_variable("short", None)
    if aba:
        await set_variable("short", False)
        await set_variable("mode", None)
        await short(client, query.message)
        await query.message.delete()
    else:
        await query.answer(
            "Invalid Input,,, Shortner is already removed", show_alert=True
        )


async def short4(client, query):
    uid = query.from_user.id
    admin1 = await get_variable("owner", "5426061889")
    admin1 = [int(x.strip()) for x in admin1.split()]
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1]

    if uid not in admin1:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

    if action == "link":
        aba = await get_variable("short", None)
        if not aba:
            await set_variable("short", True)
        await set_variable("mode", "link")
        await short(client, query.message)
        await query.message.delete()
    elif action == "24":
        while True:
            try:
                b = await query.message.edit(
                    text="⚠️ 𝐒𝐞𝐧𝐝 𝐒𝐇𝐎𝐑𝐓𝐍𝐄𝐑 𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐓𝐢𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 ----->\n"
                    "<blockquote>Xh - ꜰᴏʀ x ʜᴏᴜʀꜱ, ᴇx: 1h {ᴏɴᴇ ʜᴏᴜʀ},\n"
                    "Xm - ꜰᴏʀ x ᴍɪɴᴜᴛᴇꜱ, ᴇx: 1m {ᴏɴᴇ ᴍɪɴᴜᴛᴇ},\n"
                    "Xs - ꜰᴏʀ x ꜱᴇᴄᴏɴᴅꜱ, ᴇx: 1s {ᴏɴᴇ ꜱᴇᴄᴏɴᴅ}</blockquote>",
                    reply_markup=ReplyKeyboardMarkup(
                        [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                    ),
                )
            except BaseException:
                pass

            try:
                a = await client.listen(user_id=uid, timeout=30, chat_id=uid)

            except ListenerTimeout:
                await client.send_message(
                    chat_id=uid,
                    text="⏳ Timeout! Setup cancelled.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                break

            if a.text.lower() == "❌ cancel":
                await b.edit(
                    "❌ Timer setup cancelled.", reply_markup=ReplyKeyboardRemove()
                )
                break

            time_pattern = re.match(r"^(\d+)([hms])$", a.text.lower())

            if time_pattern:
                value, unit = int(time_pattern.group(1)), time_pattern.group(2)

                if unit == "h":
                    ab = f"{value * 3600}"  # Convert hours to seconds
                elif unit == "m":
                    ab = f"{value * 60}"  # Convert minutes to seconds
                elif unit == "s":
                    ab = str(value)  # Already in seconds
                await set_variable("token_time", ab)
                await b.delete()
                aba = await get_variable("short", None)
                if not aba:
                    await set_variable("short", True)
                await set_variable("mode", "24")
                await short(client, query.message)
                await query.message.delete()
                break
            else:
                await a.reply_text(
                    "❌ Invalid format! Try again (e.g., `1h`, `30m`, `45s`)."
                )
