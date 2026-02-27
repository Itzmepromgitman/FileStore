from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.database import get_variable, set_variable


async def protech(client, query):
    """
    Handles the callback query for protect_on and protect_off buttons.
    """
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
        await set_variable("protect", "1")
        await query.answer("✅ мαℓικ αϐ κοι ƒιℓєѕ иαнι ϲнυяαγєgα 🫡", show_alert=True)

    elif action == "off":
        await set_variable("protect", "0")
        await query.answer("✅ мαℓικ ρяοτєϲτιοи ϐαи∂ καя∂ιγα нυ... ", show_alert=True)

    else:
        # Handle unexpected action (optional)
        await query.answer("Invalid action.", show_alert=True)

    a = await get_variable("protect", "0")
    if a == "1":
        a = "✅"
        but1 = "ρяοτєϲτ ƒιℓєѕ ❌"
        call1 = "protect_off"
    else:
        but1 = "ρяοτєϲτ ƒιℓєѕ ✅"
        call1 = "protect_on"
        a = "❌"

    b = await get_variable("hide", "")
    if b == "0":
        b = "✅"
        but2 = "нι∂є ϲαρτιοи ❌"
        call2 = "hide_no"
    else:
        but2 = "нι∂є ϲαρτιοи ✅"
        call2 = "hide_yes"
        b = "❌"
    c = await get_variable("is_button", "")
    if c == "1":
        c = "✅"
    else:
        c = "❌"
    d = await get_variable("but_text", "None")
    e = await get_variable("but_link", "None")

    # Create the inline keyboard
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(but1, callback_data=call1),
                InlineKeyboardButton(but2, callback_data=call2),
            ],
            [
                InlineKeyboardButton("ѕєτ ϲαρτιοи ", callback_data="set_cap"),
                InlineKeyboardButton("ѕєτ ϐυττοи", callback_data="set_but"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    await query.message.edit_caption(
        caption=f"<blockquote>💠 𝐹𝐼𝐿𝐸𝑆 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>🔒 𝙋𝙍𝙊𝙏𝙀𝘾𝙏𝙀𝘿 𝘾𝙊𝙉𝙏𝙀𝙉𝙏: {a}\n🫥  нι∂є ϲαρτιοи : {b}\n🔘 ϲнαииєℓ ϐυττοи : {c}</blockquote>\n<blockquote>◈ ϐυττοи иαмє: {d}\n◈ ϐυττοи ℓιиκ: {e}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω",
        reply_markup=keyboard,
    )


@Client.on_callback_query(filters.regex("^hide_(no|yes)$"))
async def hitech(client, query):
    """
    Handles the callback query for protect_on and protect_off buttons.
    """
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1]

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

    if action == "yes":
        await set_variable("hide", "0")
        await query.answer("✅ ϲαρτιοи ιѕ нι∂∂єи иοω", show_alert=True)

    elif action == "no":
        await set_variable("hide", "1")
        await query.answer("✅ ϲαρτιοи ιѕ νιѕιϐℓє иοω", show_alert=True)

    else:
        # Handle unexpected action (optional)
        await query.answer("Invalid action.", show_alert=True)

    a = await get_variable("protect", "0")
    if a == "1":
        a = "✅"
        but1 = "ρяοτєϲτ ƒιℓєѕ ❌"
        call1 = "protect_off"
    else:
        but1 = "ρяοτєϲτ ƒιℓєѕ ✅"
        call1 = "protect_on"
        a = "❌"

    b = await get_variable("hide", "")
    if b == "1":
        b = "✅"
        but2 = "нι∂є ϲαρτιοи ❌"
        call2 = "hide_no"
    else:
        but2 = "нι∂є ϲαρτιοи ✅"
        call2 = "hide_yes"
        b = "❌"
    c = await get_variable("is_button", "")
    if c == "1":
        c = "✅"
    else:
        c = "❌"
    d = await get_variable("but_text", "None")
    e = await get_variable("but_link", "None")

    # Create the inline keyboard
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(but1, callback_data=call1),
                InlineKeyboardButton(but2, callback_data=call2),
            ],
            [
                InlineKeyboardButton("ѕєτ ϲαρτιοи ", callback_data="set_cap"),
                InlineKeyboardButton("ѕєτ ϐυττοи", callback_data="set_but"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    await query.message.edit_caption(
        caption=f"<blockquote>💠 𝐹𝐼𝐿𝐸𝑆 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>🔒 𝙋𝙍𝙊𝙏𝙀𝘾𝙏𝙀𝘿 𝘾𝙊𝙉𝙏𝙀𝙉𝙏: {a}\n🫥  нι∂є ϲαρτιοи : {b}\n🔘 ϲнαииєℓ ϐυττοи : {c}</blockquote>\n<blockquote>◈ ϐυττοи иαмє: {d}\n◈ ϐυττοи ℓιиκ: {e}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω",
        reply_markup=keyboard,
    )


async def setting(client, query):
    """
    Handles the callback query for protect_on and protect_off buttons.
    """

    a = await get_variable("protect", "0")
    if a == "1":
        a = "✅"
        but1 = "ρяοτєϲτ ƒιℓєѕ ❌"
        call1 = "protect_off"
    else:
        but1 = "ρяοτєϲτ ƒιℓєѕ ✅"
        call1 = "protect_on"
        a = "❌"

    b = await get_variable("hide", "")
    if b == "1":
        b = "✅"
        but2 = "нι∂є ϲαρτιοи ❌"
        call2 = "hide_no"
    else:
        but2 = "нι∂є ϲαρτιοи ✅"
        call2 = "hide_yes"
        b = "❌"
    c = await get_variable("is_button", "")
    if c == "1":
        c = "✅"
    else:
        c = "❌"
    d = await get_variable("but_text", "None")
    e = await get_variable("but_link", "None")

    # Create the inline keyboard
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(but1, callback_data=call1),
                InlineKeyboardButton(but2, callback_data=call2),
            ],
            [
                InlineKeyboardButton("ѕєτ ϲαρτιοи ", callback_data="set_cap"),
                InlineKeyboardButton("ѕєτ ϐυττοи", callback_data="set_but"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    await query.message.edit_caption(
        caption=f"<blockquote>💠 𝐹𝐼𝐿𝐸𝑆 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>🔒 𝙋𝙍𝙊𝙏𝙀𝘾𝙏𝙀𝘿 𝘾𝙊𝙉𝙏𝙀𝙉𝙏: {a}\n🫥  нι∂є ϲαρτιοи : {b}\n🔘 ϲнαииєℓ ϐυττοи : {c}</blockquote>\n<blockquote>◈ ϐυττοи иαмє: {d}\n◈ ϐυττοи ℓιиκ: {e}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω",
        reply_markup=keyboard,
    )


async def set_but(client, query):
    c = await get_variable("is_button", "")
    if c == "0":
        c = "❌"
        but1 = "υѕє ϐυττοи ✅"
        call1 = "but_on"
    else:
        c = "✅"
        but1 = "яємονє ϐυττοи ❌"
        call1 = "but_off"
    d = await get_variable("but_text", "None")
    e = await get_variable("but_link", "None")
    qua = f"<blockquote>💠 𝐵𝑈𝑇𝑇𝑂𝑁 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>⚠️ 𝑈𝑆𝐸 𝐵𝑈𝑇𝑇𝑂𝑁 : {c} </blockquote>\n<blockquote>🔰𝐵𝑈𝑇𝑇𝑂𝑁 𝑁𝐴𝑀𝐸 : {d}\n⚜𝐵𝑈𝑇𝑇𝑂𝑁 𝐿𝐼𝑁𝐾 : {e}</blockquote>\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton("ϐυττοи τєϰτ ", callback_data="set_btext"),
                InlineKeyboardButton("ϐυττοи ℓιиκ ", callback_data="set_blink"),
            ],
            [
                InlineKeyboardButton("нοмє", callback_data="setting"),
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    await query.message.edit_caption(caption=qua, reply_markup=keyboard)


async def but_on(client, query):
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1]

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

    await query.answer("Invalid action.")
    if action == "on":
        await set_variable("is_button", "1")
        await get_variable("is_button")
        await query.answer(f"✅ 𝐵𝑈𝑇𝑇𝑂𝑁 𝐼𝑆 𝑉𝐼𝑆𝐼𝐵𝐿𝐸 𝑁𝑂𝑊", show_alert=True)

    elif action == "off":
        await set_variable("is_button", "0")
        await get_variable("is_button")
        await query.answer(f"✅ 𝐵𝑈𝑇𝑇𝑂𝑁 𝐼𝑆 𝐻𝐼𝐷𝐷𝐸𝑁 𝑁𝑂𝑊 ", show_alert=True)

    else:
        # Handle unexpected action (optional)
        await query.answer("Invalid action.", show_alert=True)
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    c = await get_variable("is_button", "")
    if c == "0":
        c = "❌"
        but1 = "υѕє ϐυττοи ✅"
        call1 = "but_on"
    else:
        c = "✅"
        but1 = "яємονє ϐυττοи ❌"
        call1 = "but_off"
    d = await get_variable("but_text", "None")
    e = await get_variable("but_link", "None")
    qua = f"<blockquote>💠 𝐵𝑈𝑇𝑇𝑂𝑁 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>⚠️ 𝑈𝑆𝐸 𝐵𝑈𝑇𝑇𝑂𝑁 : {c} </blockquote>\n<blockquote>🔰𝐵𝑈𝑇𝑇𝑂𝑁 𝑁𝐴𝑀𝐸 : {d}\n⚜𝐵𝑈𝑇𝑇𝑂𝑁 𝐿𝐼𝑁𝐾 : {e}</blockquote>\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton("ϐυττοи τєϰτ ", callback_data="set_btext"),
                InlineKeyboardButton("ϐυττοи ℓιиκ ", callback_data="set_blink"),
            ],
            [
                InlineKeyboardButton("нοмє", callback_data="setting"),
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await query.message.edit_caption(caption=qua, reply_markup=keyboard)


async def set_b(client, query):

    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data
    action = query.data.split("_")[1][1:]
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    if action == "text":
        b = await client.send_message(
            uid, text="<'blockquote'>𝑃𝐿𝐸𝐴𝑆𝐸 𝑆𝐸𝑁𝐷 𝑀𝐸 𝑌𝑂𝑈 𝐵𝑈𝑇𝑇𝑂𝑁 𝑇𝐼𝑇𝐿𝐸 🌟</blockquote>"
        )
        a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
        await b.edit(f"Value {a.text} is accepted\nCheck Values at /file")
        await a.delete()
        await set_variable("but_text", a.text)

    elif action == "link":
        b = await client.send_message(
            uid, text="<blockquote>𝑃𝐿𝐸𝐴𝑆𝐸 𝑆𝐸𝑁𝐷 𝑀𝐸 𝑌𝑂𝑈 𝐵𝑈𝑇𝑇𝑂𝑁 𝐿𝐼𝑁𝐾 🌟</blockquote>"
        )
        a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
        await b.edit(f"Value {a.text} is accepted\nCheck Values at /file")
        await a.delete()
        await set_variable("but_link", a.text)


async def set_cap(client, query):
    a = await get_variable("c_caption", "0")
    if a == 1:
        a = "✅ "
        but1 = "ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ❌"
        call1 = "cap_off"
    else:
        a = "❌"
        but1 = "ᴜꜱᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ  ✅"
        call1 = "cap_on"
    b = await get_variable("cap", "None")

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton("ѕєτ ϲυѕτοм ϲαρτιοи  ", callback_data="set_ccap"),
            ],
            [
                InlineKeyboardButton("нοмє", callback_data="setting"),
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    txt = f"<blockquote expandable>💠 𝐶𝐴𝑃𝑇𝐼𝑂𝑁 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote expandable>ᴜꜱɪɴɢ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ :{a}\nᴄᴀᴘᴛɪᴏɴ ᴛᴇxᴛ : {b}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω"

    await query.message.edit_caption(caption=txt, reply_markup=keyboard)

    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")


async def cap_v(client, query):
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
        await set_variable("c_caption", "1")
        await set_variable("hide", "0")
        await query.answer(f"✅  ɪ ᴡɪʟʟ ᴜꜱᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ", show_alert=True)

    elif action == "off":
        await set_variable("c_caption", "0")

        await query.answer(f"✅  ɪ ᴡɪʟʟ ɴᴏᴛ ᴜꜱᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ", show_alert=True)

    else:
        # Handle unexpected action (optional)
        await query.answer("Invalid action.", show_alert=True)
    a = await get_variable("c_caption", "")
    if a == "1":
        a = "✅ "
        but1 = "ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ❌"
        call1 = "cap_off"
    else:
        a = "❌"
        but1 = "ᴜꜱᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ  ✅"
        call1 = "cap_on"
    b = await get_variable("cap", "None")

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton("ѕєτ ϲυѕτοм ϲαρτιοи  ", callback_data="set_ccap"),
            ],
            [
                InlineKeyboardButton("нοмє", callback_data="setting"),
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    txt = f"<blockquote expandable>💠 𝐶𝐴𝑃𝑇𝐼𝑂𝑁 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote expandable>ᴜꜱɪɴɢ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ :{a}\nᴄᴀᴘᴛɪᴏɴ ᴛᴇxᴛ : {b}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω"

    await query.message.edit_caption(caption=txt, reply_markup=keyboard)

    await query.answer("❌ ")


async def set_ccap(client, query):
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    await query.answer("❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи")
    b = await client.send_message(
        uid,
        text="<blockquote expandable>⚜ Please send me Your custom Caption Now ‼️</blockquote>\n\n<blockquote expandable>Awailable Variables 💠:-\n\n{previouscaption}:- Old captain \n{filename}:- Document file name</blockquote>\n\n\nPlease send correct formate 💠",
    )
    a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
    await b.edit(f"Value {a.text} is accepted\nCheck Values at /file")
    await a.delete()
    await set_variable("cap", a.text.html)
    a = await get_variable("c_caption", "")
    if a == "1":
        a = "✅ "
        but1 = "ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ❌"
        call1 = "cap_off"
    else:
        a = "❌"
        but1 = "ᴜꜱᴇ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ  ✅"
        call1 = "cap_on"
    b = await get_variable("cap", "None")

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(but1, callback_data=call1)],
            [
                InlineKeyboardButton("ѕєτ ϲυѕτοм ϲαρτιοи  ", callback_data="set_ccap"),
            ],
            [
                InlineKeyboardButton("нοмє", callback_data="setting"),
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )

    txt = f"<blockquote expandable>💠 𝐶𝐴𝑃𝑇𝐼𝑂𝑁 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote expandable>ᴜꜱɪɴɢ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ :{a}\nᴄᴀᴘᴛɪᴏɴ ᴛᴇxᴛ : {b}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω"

    await query.message.edit_caption(caption=txt, reply_markup=keyboard)

    await query.answer("❌ ")
