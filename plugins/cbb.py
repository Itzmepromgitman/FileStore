# (©)Codexbotz

from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from database.database import get_variable


@Client.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text="♻️",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            ),
        )
        raw_channels = await get_variable(
            "F_sub", "-1002374561133 -1002252580234 -1002359972599"
        )
        fsub = [int(x.strip()) for x in raw_channels.split()]
        raw_data = await get_variable("r_sub", "")
        if not raw_data:
            raw_data = ""
        rsub = []
        for entry in raw_data.strip().split(","):
            if entry:
                try:
                    chat_id, invite_link = entry.split("||")
                    rsub.append((int(chat_id), invite_link))
                except ValueError:
                    continue
        await query.message.edit_text(
            text="♻️♻️",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            ),
        )
        admin = await get_variable("admin", [])
        print(admin)
        ifdel = await get_variable("del", "0")
        if ifdel == "1":
            dele = "ᴇɴᴀʙʟᴇᴅ"
        else:
            dele = "ᴅɪsᴀʙʟᴇᴅ"
        prot = await get_variable("protect", "0")
        if prot == "1":
            prot = "ᴇɴᴀʙʟᴇᴅ"
        else:
            prot = "ᴅɪsᴀʙʟᴇᴅ"
        but = await get_variable("is_button", "0")
        await query.message.edit_text(
            text="♻️♻️♻️",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            ),
        )
        if but == "1":
            but = "ᴇɴᴀʙʟᴇᴅ"
        else:
            but = "ᴅɪsᴀʙʟᴇᴅ"
        hide = await get_variable("hide", "1")
        if hide == "0":
            hide = "ᴇɴᴀʙʟᴇᴅ"
        else:
            hide = "ᴅɪsᴀʙʟᴇᴅ"
        await query.message.edit_text(
            text=f"""<b>✇ ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴs</b><blockquote><b>╭━━══════════════○\n┣➣ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ:  {len(fsub)}\n┣➣ ᴀᴅᴍɪɴs:  {len(admin)}\n┣➣ ʙᴀɴɴᴇᴅ ᴜsᴇʀs:  0\n┣➣ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴏᴅᴇ:  {dele}\n┣➣ ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ:  {prot}\n┣➣ ʜɪᴅᴇ ᴄᴀᴘᴛɪᴏɴ:  {hide}\n┣➣ ᴄʜᴀɴɴᴇʟ ʙᴜᴛᴛᴏɴ:  {but}\n┣➣ ʀᴇǫᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ: {len(rsub)}\n╰━━══════════════○</b></blockquote>""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
    query.continue_propagation()
