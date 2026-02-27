from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.database import get_variable


async def files(client, message):

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

    await message.reply_photo(
        "https://i.ibb.co/dq5qd2R/x.jpg",
        caption=f"<blockquote>💠 𝐹𝐼𝐿𝐸𝑆 𝑆𝐸𝑇𝑇𝐼𝑁𝐺𝑆 ♻️</blockquote>\n<blockquote>🔒 𝙋𝙍𝙊𝙏𝙀𝘾𝙏𝙀𝘿 𝘾𝙊𝙉𝙏𝙀𝙉𝙏: {a}\n🫥  нι∂є ϲαρτιοи : {b}\n🔘 ϲнαииєℓ ϐυττοи : {c}</blockquote>\n<blockquote>◈ ϐυττοи иαмє: {d}\n◈ ϐυττοи ℓιиκ: {e}</blockquote>\n\nυѕє τнє ϐυττοиѕ gινєи ϐєℓοω",
        reply_markup=keyboard,
    )


@Client.on_callback_query(filters.regex("protect_on"))
async def protect_on_callback(client, callback_query):
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    # Optional: Show a notification
    await callback_query.answer("Protect is now ON!")
    await callback_query.message.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Protect Yes", callback_data="protect_off"),
                    InlineKeyboardButton(
                        "Channel Button No", callback_data="button_on"
                    ),  # Assuming you want to keep the other button as is
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("protect_off"))
async def protect_off_callback(client, callback_query):
    # Handle the "protect off" callback
    # Update the 'protext' variable (e.g., in your database or config file)
    # For example:
    # await set_variable("protext", "False")  # Assuming you have a
    # set_variable function
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    # Optional: Show a notification
    await callback_query.answer("Protect is now OFF!")
    await callback_query.message.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Protect No", callback_data="protect_on"),
                    InlineKeyboardButton(
                        "Channel Button No", callback_data="button_on"
                    ),  # Assuming you want to keep the other button as is
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("button_on"))
async def button_on_callback(client, callback_query):
    # Handle the "button on" callback
    # Update the 'button' variable (e.g., in your database or config file)
    # For example:
    # await set_variable("button", "True")  # Assuming you have a set_variable
    # function
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    # Optional: Show a notification
    await callback_query.answer("Channel Button is now ON!")
    await callback_query.message.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Protect No", callback_data="protect_on"),
                    InlineKeyboardButton(
                        "Channel Button Yes", callback_data="button_off"
                    ),  # Assuming you want to keep the other button as is
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("button_off"))
async def button_off_callback(client, callback_query):
    # Handle the "button off" callback
    # Update the 'button' variable (e.g., in your database or config file)
    # For example:
    # await set_variable("button", "False")  # Assuming you have a
    # set_variable function
    uid = query.from_user.id
    admin = await get_variable("admin", [])
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return
    # Optional: Show a notification
    await callback_query.answer("Channel Button is now OFF!")
    await callback_query.message.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Protect No", callback_data="protect_on"),
                    InlineKeyboardButton(
                        "Channel Button No", callback_data="button_on"
                    ),  # Assuming you want to keep the other button as is
                ]
            ]
        )
    )
