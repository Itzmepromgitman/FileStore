import pyrogram.utils
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOGGER

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
pyrogram.utils.MAX_CHANNEL_ID = -1000000000000
log = LOGGER(__name__)


async def prem(client, query):
    log.info("function works")
    text = "🌟 <b>Premium Access</b> 🌟<b>\n</b><blockquote expandable><b><i>🔥 Elevate your experience with Premium Access! 🔥</i></b></blockquote>\n\n<b>💸 ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs:\n➥ ₹10 - </b>1 ᴅᴀʏ ᴀᴄᴄᴇss <b>\n➥ ₹50 - </b>2 ᴡᴇᴇᴋs ᴀᴄᴄᴇss<b> \n➥ ₹100 - </b>1 ᴍᴏɴᴛʜ ᴀᴄᴄᴇss<b>\n➥ ₹699 - </b>1 ʏᴇᴀʀ ᴀᴄᴄᴇss\n\n<blockquote expandable>🛍 <b>ʜᴏᴡ ᴛᴏ ᴘᴜʀᴄʜᴀsᴇ ᴘʀᴇᴍɪᴜᴍ -</b>\n\n💫 <b>sᴄᴀɴ</b> ᴛʜᴇ ǫʀ ᴄᴏᴅᴇ Ꭺʙᴏvᴇ.\n💫 <b>sᴇɴᴅ</b> ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴛʜᴇ ᴘʟᴀɴ ʏᴏᴜ ᴡᴀɴᴛ.\n💫 <b>ʀᴇᴘᴏʀᴛ</b> ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ ᴛᴏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴜsɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ!                                              \n</blockquote>📨 𝚄𝙿𝙸 𝙸𝙳: a.compss.pandey@fam\n\n<blockquote expandable>🎉 <i>Premium Benefits:\n🔅Unlimited Access\n🔅 No Ads\n🔅 Faster Experience\n🔅 Priority Support</i>                                            </blockquote>\n\n<b>⚠️ </b>ɪᴍᴘᴏʀᴛᴀɴᴛ ɴᴏᴛᴇ ⚠️:\n📌 <i>Send the correct amount as per the plan.\n📌 No refunds once the transaction is make.</i>\n\n<blockquote expandable><b><i>🙌 Success starts when you invest in yourself. Unlock the best with Premium.</i></b></blockquote>"
    key = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ꜱᴇɴᴅ ᴘʀᴏᴏꜰ 🗞️", url="t.me/reactiveargon")],
            [InlineKeyboardButton("ᴄᴀɴᴄᴇʟ ", callback_data=f"close")],
        ]
    )
    await query.message.delete()
    await client.send_photo(
        photo="https://i.postimg.cc/7L21CDbc/image-2x-1.png",
        caption=text,
        reply_markup=key,
        chat_id=query.from_user.id,
    )
