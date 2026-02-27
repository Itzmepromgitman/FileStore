import re

from pyrogram.errors.pyromod.listener_timeout import ListenerTimeout
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from database.database import get_variable, set_variable


async def del1(client, message):
    a = await get_variable("del", "0")
    if a == "1":
        a = "✅"
        but1 = "𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞  ❌"
        call1 = "del_off"
    else:
        but1 = "𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞  ✅"
        call1 = "del_on"
        a = "❌"
    b = await get_variable("del_timer", 0)  # Get the time (string)
    total_seconds = int(b)  # Convert to integer

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

    b = " ".join(time_parts) if time_parts else "0 seconds"

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton(
                    "┈━═☆ Sєτ ∂єℓєτє τιмє ☆═━┈", callback_data="set_del"
                )
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    txt = (
        f"<blockquote>⚜ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ꜱᴇᴛᴛɪɴɢꜱ ♻️</blockquote>\n"
        f"<blockquote>ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ - {a}</blockquote>\n"
        f"<blockquote>ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ: {b}</blockquote>\n"
        "⚠️ 𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐓𝐢𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 ----->\n"
        "<blockquote>"
        "Xh - ꜰᴏʀ x ʜᴏᴜʀꜱ, ᴇx: 1h {ᴏɴᴇ ʜᴏᴜʀ}\n"
        "Xm - ꜰᴏʀ x ᴍɪɴᴜᴛᴇꜱ, ᴇx: 1m {ᴏɴᴇ ᴍɪɴᴜᴛᴇ}\n"
        "Xs - ꜰᴏʀ x ꜱᴇᴄᴏɴᴅꜱ, ᴇx: 1s {ᴏɴᴇ ꜱᴇᴄᴏɴᴅ}"
        "</blockquote>"
    )

    await message.reply_photo(
        photo="https://i.ibb.co/mC9pszgP/x.jpg", caption=txt, reply_markup=keyboard
    )


async def del2(client, query):
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1]

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

    if action == "on":
        await set_variable("del", "1")
        await query.answer(f"✅  ɪ ᴡɪʟʟ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ", show_alert=True)

    elif action == "off":
        await set_variable("del", "0")
        await query.answer(f"✅  ɪ ᴡɪʟʟ ɴᴏᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ", show_alert=True)

    a = await get_variable("del", "0")
    if a == "1":
        a = "✅"
        but1 = "𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞  ❌"
        call1 = "del_off"
    else:
        but1 = "𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞  ✅"
        call1 = "del_on"
        a = "❌"
    b = await get_variable("del_timer", "0")  # Get the time (string)
    total_seconds = int(b)  # Convert to integer

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

    b = " ".join(time_parts) if time_parts else "0 seconds"

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton(
                    "┈━═☆ Sєτ ∂єℓєτє τιмє ☆═━┈", callback_data="set_del"
                )
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    txt = (
        f"<blockquote>⚜ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ꜱᴇᴛᴛɪɴɢꜱ ♻️</blockquote>\n"
        f"<blockquote>ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ - {a}</blockquote>\n"
        f"<blockquote>ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ: {b}</blockquote>\n"
        "⚠️ 𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐓𝐢𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 ----->\n"
        "<blockquote>"
        "Xh - ꜰᴏʀ x ʜᴏᴜʀꜱ, ᴇx: 1h {ᴏɴᴇ ʜᴏᴜʀ}\n"
        "Xm - ꜰᴏʀ x ᴍɪɴᴜᴛᴇꜱ, ᴇx: 1m {ᴏɴᴇ ᴍɪɴᴜᴛᴇ}\n"
        "Xs - ꜰᴏʀ x ꜱᴇᴄᴏɴᴅꜱ, ᴇx: 1s {ᴏɴᴇ ꜱᴇᴄᴏɴᴅ}"
        "</blockquote>"
    )

    await query.message.edit_caption(caption=txt, reply_markup=keyboard)


async def del3(client, query):
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    while True:
        b = await client.send_message(
            uid,
            text="⚠️ 𝐒𝐞𝐧𝐝 𝐀𝐮𝐭𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐓𝐢𝐦𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 ----->\n"
            "<blockquote>Xh - ꜰᴏʀ x ʜᴏᴜʀꜱ, ᴇx: 1h {ᴏɴᴇ ʜᴏᴜʀ},\n"
            "Xm - ꜰᴏʀ x ᴍɪɴᴜᴛᴇꜱ, ᴇx: 1m {ᴏɴᴇ ᴍɪɴᴜᴛᴇ},\n"
            "Xs - ꜰᴏʀ x ꜱᴇᴄᴏɴᴅꜱ, ᴇx: 1s {ᴏɴᴇ ꜱᴇᴄᴏɴᴅ}</blockquote>",
            reply_markup=ReplyKeyboardMarkup(
                [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
            ),
        )

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
            await b.delete()
            await client.send_message(
                chat_id=uid,
                text="❌ Timer setup cancelled.",
                reply_markup=ReplyKeyboardRemove(),
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
            await set_variable("del_timer", ab)
            await client.send_message(
                chat_id=uid,
                text=f"✅ Value `{a.text}` is accepted\nCheck Values at /auto_del",
                reply_markup=ReplyKeyboardRemove(),
            )
            await a.delete()
            break  # Exit loop after a valid input
        else:
            await a.reply_text(
                "❌ Invalid format! Try again (e.g., `1h`, `30m`, `45s`)."
            )
