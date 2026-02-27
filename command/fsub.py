import re

import pyrogram.utils
from pyrogram.errors import ChannelPrivate, ChatAdminRequired, RPCError
from pyrogram.errors.pyromod.listener_timeout import ListenerTimeout
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from config import LOGGER
from database.database import get_variable, set_variable

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
pyrogram.utils.MAX_CHANNEL_ID = -1000000000000

log = LOGGER(__name__)


async def onreq(client, join_request):
    invite_link = join_request.invite_link
    req_link = await get_variable("req_link", []) or []

    if invite_link.invite_link in req_link:
        link = await get_variable(f"{invite_link.invite_link}", []) or []
        if join_request.from_user.id not in link:
            link.append(join_request.from_user.id)
            await set_variable(f"{invite_link.invite_link}", link)
            work = await get_variable(f"req{invite_link.invite_link}", 0) or 0
            work = int(work) if work not in (None, "None") else 0
            work += 1
            await set_variable(f"req{invite_link.invite_link}", work)


async def fsub1(client, message):
    a = await message.reply_text("processing")
    raw_channels = await get_variable(
        "F_sub", "-1002374561133 -1002252580234 -1002359972599"
    )
    FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]
    raw_data = await get_variable("r_sub", "")
    if not raw_data:
        raw_data = ""
    channels = []
    for entry in raw_data.strip().split(","):
        if entry:
            try:
                chat_id, invite_link = entry.split("||")
                channels.append((int(chat_id), invite_link))
            except ValueError:
                continue
    fsub_text = "<blockquote>⚜ 𝐅𝐨𝐫𝐜𝐞 𝐒𝐮𝐛 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 ♻️</blockquote>\n"
    fsub_text += "<blockquote expandable>┏━━━•❅•°•❈ 𝐍𝐨𝐫𝐦𝐚𝐥 𝐅𝐬𝐮𝐛 •°•❅•━━┓\n\n"
    owner = await get_variable("owner", [])
    for index, channel_id in enumerate(FORCE_SUB_CHANNELS, start=1):
        try:
            chat = await client.get_chat(int(channel_id))
            title = chat.title
            subscriber_count = chat.members_count
            fsub_text += f"{index}. {title}\n"
            fsub_text += f"   ├─ Total Subscribers: {subscriber_count}\n"
            fsub_text += f"   └─ ID: <code>{channel_id}</code>\n\n"
        except ChatAdminRequired:
            fsub_text += f"{index}. ❌ Bot lacks admin rights in the channel (ID: <code>{channel_id}</code>)\n"
        except ChannelPrivate:
            fsub_text += f"{index}. ❌ Channel is private or the bot is banned (ID: <code>{channel_id}</code>)\n"
        except RPCError:
            fsub_text += f"{index}. ❌ Bot is not in the channel or cannot access it (ID: <code>{channel_id}</code>)"
        except ValueError:
            try:
                for ids in owner:
                    await client.send_message(
                        ids, f"Please send some message on channel id = {channel_id}"
                    )
            except BaseException:
                pass
    fsub_text += "┗━━━━━━━━━━━━━━━━━━━━━┛</blockquote>\n"
    fsub_text += "<blockquote expandable>┏━━━•❅•°•❈ 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐅𝐬𝐮𝐛 •°•❅•━━┓\n\n"
    for index, (channel_id, link) in enumerate(channels, start=1):
        try:
            ab = await get_variable(f"req{link}", "None")
            link = re.sub(r"^https://", "", link)
            chat = await client.get_chat(channel_id)
            title = chat.title
            subscriber_count = chat.members_count
            fsub_text += f"{index}. {title}\n"
            fsub_text += f"   ├─ Total Subscribers: {subscriber_count}\n"
            fsub_text += f"   ├─ ID: <code>{channel_id}</code>\n"
            fsub_text += f"   ├─ Link: <code>{link}</code>\n"
            fsub_text += f"   └─ Requests: {ab}\n\n"
        except ChatAdminRequired:
            fsub_text += f"{index}. ❌ Bot lacks admin rights in the channel (ID: <code>{channel_id}</code>)\n"
        except ChannelPrivate:
            fsub_text += f"{index}. ❌ Channel is private or the bot is banned (ID: <code>{channel_id}</code>)\n"
        except RPCError:
            fsub_text += f"{index}. ❌ Bot is not in the channel or cannot access it (ID: <code>{channel_id}</code>)"
    fsub_text += "┗━━━━━━━━━━━━━━━━━━━━━┛</blockquote>\n"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐀𝐃𝐃 𝐅𝐒𝐔𝐁", callback_data="fsub_add"),
                InlineKeyboardButton("𝐑𝐄𝐌𝐎𝐕𝐄 𝐅𝐒𝐔𝐁", callback_data="fsub_rem"),
            ],
            [
                InlineKeyboardButton("𝐀𝐃𝐃 𝐑𝐒𝐔𝐁", callback_data="rsub_add"),
                InlineKeyboardButton("𝐑𝐄𝐌𝐎𝐕𝐄 𝐑𝐒𝐔𝐁", callback_data="rsub_rem"),
            ],
            [
                InlineKeyboardButton("ϲℓοѕє", callback_data="close"),
            ],
        ]
    )
    await a.delete()
    await message.reply_photo(
        photo="https://i.ibb.co/YBLs424Q/x.jpg",
        caption=fsub_text,
        reply_markup=keyboard,
    )


async def fsub2(client, query):
    txt = (
        "<blockquote expandable>⚠️ <b>𝖣𝗈 𝖮𝗇𝖾 𝖡𝖾𝗅𝗈𝗐</b>  ⚠️</blockquote>\n"
        "<blockquote expandable><i>🔱 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗋𝗈𝗆 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</i></blockquote>\n"
        "<blockquote expandable><i>💠 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖽</i></blockquote>"
        "<blockquote>♨️ 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗗𝗠𝗜𝗡  ♨️</blockquote>"
    )
    uid = query.from_user.id
    user_id = uid
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

    while True:
        try:
            b = await client.send_message(
                uid,
                text=txt,
                reply_markup=ReplyKeyboardMarkup(
                    [["❌ Cancel"]], one_time_keyboard=True, resize_keyboard=True
                ),
            )

            a = await client.listen(user_id=uid, timeout=30, chat_id=uid)
        except ListenerTimeout:
            await client.send_message(
                chat_id=uid,
                text="⏳ Timeout! Fsub Setup cancelled.",
                reply_markup=ReplyKeyboardRemove(),
            )
            await b.delete()
            break
        except Exception as e:
            log.error(e, exc_info=True)
        forward_origin = a.forward_origin
        if forward_origin:
            if forward_origin.chat:
                chat_id = forward_origin.chat.id
            elif forward_origin.sender_chat:
                chat_id = forward_origin.sender_chat.id

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
                if not str(chat_id).startswith("-10"):
                    await client.send_message(
                        user_id, "Invalid Channel/Group ID! Please send a valid one."
                    )
                    await b.delete()
                    continue  # Ask again
            except ValueError:
                await client.send_message(
                    user_id, "Invalid input! Please send a valid channel/group ID."
                )
                await b.delete()
                continue
        try:
            # Get bot's status
            chat_member = await client.get_chat_member(chat_id, "me")
            if chat_member.status not in ["administrator", "owner"]:
                await a.delete()
                await b.edit(
                    "I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID "
                )
                await b.delete
                continue
        except Exception as e:
            if "USER_NOT_PARTICIPANT" in str(e):
                await client.send_message(
                    user_id,
                    f"I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID \n\n```python\n{e}```",
                )
                log.error(e, exc_info=True)
                await b.delete()
                continue
        try:
            chat_member = await client.get_chat_member(chat_id, "me")
            if not chat_member.privileges.can_invite_users:
                await client.send_message(
                    user_id,
                    "I need the 'Invite Users' permission! Please enable it in channel settings. \n\nResend The Id After permissions",
                )
                await b.delete()
                continue
        except Exception as e:
            await client.send_message(
                user_id,
                f"I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID \n\n```python\n{e}```",
                log.error(e, exc_info=True),
            )
            continue
        try:
            await b.delete()
            raw_channels = await get_variable(
                "F_sub", "-1002374561133 -1002252580234 -1002359972599"
            )
            FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]
            if chat_id not in FORCE_SUB_CHANNELS:
                FORCE_SUB_CHANNELS.append(chat_id)

                # Convert back to a space-separated string
                updated_channels = " ".join(map(str, FORCE_SUB_CHANNELS))

                # Save the updated list
                await set_variable("F_sub", updated_channels)
                await client.send_message(
                    user_id,
                    "𝙁𝙎𝙐𝘽 𝘼𝘿𝘿𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔 ✅ ",
                    reply_markup=ReplyKeyboardRemove(),
                )
            else:
                await client.send_message(
                    user_id,
                    f"Channel {chat_id} is already in the list.",
                    reply_markup=ReplyKeyboardRemove(),
                )
            await fsub1(client, query.message)
            await query.message.delete()
            break

        except ChatAdminRequired:
            await client.send_message(
                user_id,
                "I don't have access to check admin permissions! Please add me first. \\ After that Resend The ID",
            )


async def fsub3(client, query):
    txt = (
        "<blockquote expandable>⚠️ <b>𝖣𝗈 𝖮𝗇𝖾 𝖡𝖾𝗅𝗈𝗐</b>  ⚠️</blockquote>\n"
        "<blockquote expandable><i>🔱 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗋𝗈𝗆 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</i></blockquote>\n"
        "<blockquote expandable><i>💠 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖽</i></blockquote>"
    )

    uid = query.from_user.id
    user_id = uid
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

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
                if not str(chat_id).startswith("-10"):
                    await client.send_message(
                        user_id, "Invalid Channel/Group ID! Please send a valid one."
                    )
                    await b.delete()
                    continue  # Ask again
            except ValueError:
                await client.send_message(
                    user_id, "Invalid input! Please send a valid channel/group ID."
                )
                await b.delete()
                continue

        raw_channels = await get_variable(
            "F_sub", "-1002374561133 -1002252580234 -1002359972599"
        )
        FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]
        if chat_id in FORCE_SUB_CHANNELS:
            FORCE_SUB_CHANNELS.remove(chat_id)

            # Convert back to a space-separated string
            updated_channels = " ".join(map(str, FORCE_SUB_CHANNELS))

            # Save the updated list
            await set_variable("F_sub", updated_channels)

            await client.send_message(
                user_id,
                "𝙁𝙎𝙐𝘽 𝙍𝙀𝙈𝙊𝙑𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔 ✅ ",
                reply_markup=ReplyKeyboardRemove(),
            )
            await fsub1(client, query.message)
            await query.message.delete()
            await b.delete()
            break

        else:
            await client.send_message(
                user_id,
                f"<blockquote>Channel {chat_id} is not present in F Sub list ❌ \n Please resend Value</blockquote>",
                reply_markup=ReplyKeyboardRemove(),
            )


async def fsub4(client, query):
    txt = (
        "<blockquote expandable>⚠️ <b>𝖣𝗈 𝖮𝗇𝖾 𝖡𝖾𝗅𝗈𝗐</b>  ⚠️</blockquote>\n"
        "<blockquote expandable><i>🔱 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗋𝗈𝗆 R𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</i></blockquote>\n"
        "<blockquote expandable><i>💠 𝖲𝖾𝗇𝖽 𝖬𝖾 R𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖽</i></blockquote>"
        "<blockquote>♨️ 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗗𝗠𝗜𝗡  ♨️</blockquote>"
    )
    uid = query.from_user.id
    user_id = uid
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

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
                if not str(chat_id).startswith("-10"):
                    await client.send_message(
                        user_id, "Invalid Channel/Group ID! Please send a valid one."
                    )
                    await b.delete()
                    continue  # Ask again
            except ValueError:
                await client.send_message(
                    user_id, "Invalid input! Please send a valid channel/group ID."
                )
                await b.delete()
                continue
        try:
            # Get bot's status
            chat_member = await client.get_chat_member(chat_id, "me")
            if chat_member.status not in ["administrator", "owner"]:
                await a.delete()
                await b.edit(
                    "I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID "
                )
                await b.delete
                continue
            else:
                b.edit(f"Chat status:-{chat_member.status}")
        except Exception as e:
            if "USER_NOT_PARTICIPANT" in str(e):
                await client.send_message(
                    user_id,
                    f"I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID \n\n```python\n{e}```",
                )
                log.error(e, exc_info=True)
                await b.delete()
                continue
        try:
            # Check if bot has invite user permissions
            if not chat_member.privileges.can_invite_users:
                await client.send_message(
                    user_id,
                    "I need the 'Invite Users' permission! Please enable it in channel settings. \n\nResend The Id After permissions",
                )
                await b.delete()
                continue
        except Exception as e:
            await client.send_message(
                user_id,
                f"I'm not an admin in this channel! Please add me as an admin.\n \nPlease Add me as admin and resend the ID \n\n```python\n{e}```",
            )
            log.error(e, exc_info=True)
            continue
        try:
            await b.delete()
            raw_channels = await get_variable("r_sub")
            if raw_channels:
                existing_channels = [
                    int(x.split("||")[0].strip()) for x in raw_channels.split(",") if x
                ]
            else:
                existing_channels = []
            try:
                chat = await client.get_chat(chat_id)
                if chat.username:
                    await client.send_message(
                        user_id,
                        f"❌ Public Channels Are Not Accepted In Rsub.\n Resend",
                    )
                    continue
                if chat_id in existing_channels:
                    await client.send_message(
                        user_id,
                        f"❌ Channel {chat_id} is already in the list of Rsub.\nPlease resend",
                        reply_markup=ReplyKeyboardRemove(),
                    )
                    continue
                invite_link = await client.create_chat_invite_link(
                    chat_id, creates_join_request=True
                )
                req_link = await get_variable("req_link", [])

                req_link.append(invite_link.invite_link)
                await set_variable("req_link", req_link)
                new_entry = f"{chat_id}||{invite_link.invite_link},"
                new_value = f"{raw_channels}{new_entry}" if raw_channels else new_entry
                await set_variable("r_sub", new_value)
                await client.send_message(
                    user_id,
                    "𝙍𝙎𝙐𝘽 𝘼𝘿𝘿𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔 ✅",
                    reply_markup=ReplyKeyboardRemove(),
                )

            except Exception as e:
                log.info(f"Error: {str(e)}")
            await fsub1(client, query.message)
            await query.message.delete()
            break
        except ChatAdminRequired:
            await client.send_message(
                user_id,
                "I don't have access to check admin permissions! Please add me first. \\ After that Resend The ID",
            )
        except Exception as e:
            log.error(e, exc_info=True)


async def fsub5(client, query):
    txt = (
        "<blockquote expandable>⚠️ <b>𝖣𝗈 𝖮𝗇𝖾 𝖡𝖾𝗅𝗈𝗐</b>  ⚠️</blockquote>\n"
        "<blockquote expandable><i>🔱 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖥𝗋𝗈𝗆 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</i></blockquote>\n"
        "<blockquote expandable><i>💠 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖥𝗌𝗎𝖻 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖨𝖽</i></blockquote>"
    )

    uid = query.from_user.id
    user_id = uid
    admin = await get_variable(
        "owner", "-1002374561133 -1002252580234 -1002359972599 5426061889"
    )
    admin = [int(x.strip()) for x in admin.split()]
    # Extract "on" or "off" from the callback data

    if uid not in admin:
        await query.answer(
            "❌ ϐακκα!, γου αяє иοτ αℓℓοωє∂ το υѕє τнє ϐυττοи", show_alert=True
        )
        return

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
                if not str(chat_id).startswith("-10"):
                    await client.send_message(
                        user_id, "Invalid Channel/Group ID! Please send a valid one."
                    )
                    await b.delete()
                    continue  # Ask again
            except ValueError:
                await client.send_message(
                    user_id, "Invalid input! Please send a valid channel/group ID."
                )
                await b.delete()
                continue

        raw_channels = await get_variable("r_sub")
        if not raw_channels:
            await client.send_message(
                user_id,
                f"<blockquote>Channel {chat_id} is not present in F Sub list ❌ \n Please resend Value</blockquote>",
                reply_markup=ReplyKeyboardRemove(),
            )
            continue

        entries = raw_channels.split(",")
        lonk = None
        updated_channels = []

        for entry in entries:
            if entry and entry.startswith(f"{chat_id}||"):
                lonk = entry.split("||")[1]  # Extract the invite link
            else:
                updated_channels.append(entry)

        if lonk is None:  # If chat_id was not found
            await client.send_message(
                user_id,
                f"<blockquote>Channel {chat_id} is not present in F Sub list ❌ \n Please resend Value</blockquote>",
                reply_markup=ReplyKeyboardRemove(),
            )
            continue

        # Update the variable after removing the channel entry
        new_value = ",".join(updated_channels)
        await set_variable("r_sub", new_value)

        # Remove the associated variables
        await set_variable(lonk, None)
        await set_variable(f"req{lonk}", 0)
        links = await get_variable("req_link", [])
        if lonk in links:
            links.remove(lonk)
        await set_variable("req_link", links)

        # Send confirmation message
        await client.send_message(
            user_id, "𝙍𝙎𝙐𝘽 𝙍𝙀𝙈𝙊𝙑𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔 ✅", reply_markup=ReplyKeyboardRemove()
        )

        # Trigger fsub1 function and clean up messages
        await fsub1(client, query.message)
        await query.message.delete()
        await b.delete()
        break
