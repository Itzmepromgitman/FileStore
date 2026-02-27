import random
from datetime import datetime, timedelta

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChannelPrivate,
    ChatAdminRequired,
    RPCError,
    UserNotParticipant,
)
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import LOGGER, images
from database.database import add_user, get_variable, present_user, set_variable

log = LOGGER(__name__)


async def not_subscribed(c, a, message, user_id=False):
    if not user_id:
        user_id = message.from_user.id
    ab = await message.reply_text("❗️ Checking subscription...")

    # Get forced channels
    try:
        raw_fsub = await get_variable(
            "F_sub", "-1002374561133 -1002252580234 -1002359972599"
        )
        FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_fsub.split()]
        log.info(f"Forced subscription channels: %s", FORCE_SUB_CHANNELS)
    except Exception as e:
        log.error("Error fetching F_sub variable: %s", e, exc_info=True)
        await ab.delete()
        return True

    # Check: Must be in all FORCE_SUB_CHANNELS
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await a.get_chat_member(channel, user_id)
            log.info(f"User %s status in channel %s: %s", user_id, channel, user.status)
            if user.status not in {
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.RESTRICTED,
            }:
                log.warning("User %s not in forced channel %s", user_id, channel)
                await ab.delete()
                return True
        except UserNotParticipant:
            log.warning(
                "User %s is not participant in forced channel %s", user_id, channel
            )
            await ab.delete()
            return True
        except (ChatAdminRequired, RPCError, ChannelPrivate) as e:
            log.error("Skipped forced channel %s check due to error: %s", channel, e)
            continue

    # Check entries in r_sub
    try:
        raw_channels_data = await get_variable("r_sub", "")
        log.info("Raw r_sub data: %r", raw_channels_data)
        channel_entries = [x.strip() for x in raw_channels_data.split(",") if x]
        log.info(f"Parsed r_sub entries: %s", channel_entries)
    except Exception as e:
        log.error("Error fetching r_sub variable: %s", e, exc_info=True)
        await ab.delete()
        return True

    for entry in channel_entries:
        log.info("Processing entry: %s", entry)
        try:
            chan_id_str, invite_link = entry.split("||")
            chan_id = int(chan_id_str.strip())
            invite_link = invite_link.strip()
        except ValueError as e:
            log.error("Malformed entry '%s': %s", entry, e)
            continue

        in_channel = False
        in_invite_list = False

        # Check if user is in channel
        try:
            user = await a.get_chat_member(chan_id, user_id)
            log.info(
                "User %s status in r_sub channel %s: %s", user_id, chan_id, user.status
            )
            if user.status in {
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.RESTRICTED,
            }:
                in_channel = True
        except UserNotParticipant:
            log.info("User %s not in r_sub channel %s", user_id, chan_id)
        except (ChatAdminRequired, RPCError, ChannelPrivate) as e:
            log.error("Error checking membership in r_sub channel %s: %s", chan_id, e)
            in_channel = True

        # Check if user is in invite list
        try:
            invite_users = await get_variable(invite_link, [])
            log.info("Invite list for '%s': %s", invite_link, invite_users)
            if user_id in invite_users:
                in_invite_list = True
        except Exception as e:
            log.error("Error fetching invite list '%s': %s", invite_link, e)

        # User must be in either the channel or the invite list
        if not in_channel and not in_invite_list:
            log.warning(
                "User %s missing subscription for channel %s or invite '%s'",
                user_id,
                chan_id,
                invite_link,
            )
            await ab.delete()
            return True
        else:
            log.info("User %s passed subscription check for entry %s", user_id, entry)

    # All checks passed
    await ab.delete()
    log.info("User %s passed all subscription checks", user_id)
    return False  # User passes all checks


all


async def subscribed(_, a, message, q=False):
    user_id = message.from_user.id
    if q:
        user_id = q.from_user.id
    ab = await message.reply_text("❗️")

    # Get forced channels
    raw_fsub = await get_variable(
        "F_sub", "-1002374561133 -1002252580234 -1002359972599"
    )
    FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_fsub.split()]
    log.info(user_id)
    # Check: Must be in all FORCE_SUB_CHANNELS
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await a.get_chat_member(channel, user_id)

            if user.status not in {
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.RESTRICTED,
            }:
                await ab.delete()
                return False
        except UserNotParticipant:
            await ab.delete()
            return False
        except (ChatAdminRequired, RPCError, ChannelPrivate):
            continue

    # Check entries in r_sub
    raw_channels_data = await get_variable("r_sub", "")
    channel_entries = [x.strip() for x in raw_channels_data.split(",") if x]

    for entry in channel_entries:
        try:
            chan_id, invite_link = entry.split("||")
            chan_id = int(chan_id.strip())
            invite_link = invite_link.strip()
        except ValueError:
            continue  # Skip malformed entries

        in_channel = False
        in_invite_list = False

        # Check if user is in channel
        try:
            user = await a.get_chat_member(chan_id, user_id)
            if user.status in {
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.RESTRICTED,
            }:
                in_channel = True
        except UserNotParticipant:
            pass
        except (ChatAdminRequired, RPCError, ChannelPrivate):
            in_channel = True

        # Check if user is in invite list
        try:
            invite_users = await get_variable(invite_link, [])
            if user_id in invite_users:
                in_invite_list = True
        except Exception:
            pass

        # User must be in either the channel or the invite list
        if not in_channel and not in_invite_list:
            await ab.delete()
            return False  # Not subscribed

    await ab.delete()
    return True  # User passes all checks


async def force_subs(client, message):
    IMAGE_URL = random.choice(images)
    raw_channels = await get_variable(
        "F_sub", "-1002374561133 -1002252580234 -1002359972599"
    )
    FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]
    user_iddd = message.from_user.id
    user_id = user_iddd
    a = await message.reply_text("♻️")
    text = message.text

    if 50 > len(text) > 7:
        try:
            string = text.split(" ", 1)[1]
        except BaseException:
            string = ""
    else:
        string = ""

    # Check if the user exists in your database
    if not await present_user(user_iddd):
        # Add the user to the database
        await add_user(user_iddd)

    not_joined_channels = []
    buttons = []
    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)
        except Exception as e:
            print(f"{e}")

    await a.edit("♻️♻️️️")
    for channel in not_joined_channels:
        if str(channel).startswith("-100"):  # Private or ID-based channel
            chat = await client.get_chat(channel)
            try:
                # Create a 1-minute expiry invite link
                expire_time = datetime.utcnow() + timedelta(minutes=1)
                invite = await client.create_chat_invite_link(
                    chat_id=channel, expire_date=expire_time
                )
                invite_link = invite.invite_link
            except Exception:
                invite_link = None

            # fallback link if export fails
            link = invite_link or f"https://t.me/c/{channel[4:]}"
            name = chat.title or "Channel"
        else:  # Public channel
            link = f"https://t.me/{channel}"
            name = channel

        buttons.append([InlineKeyboardButton(text=f"• ᴊᴏɪɴ {name} •", url=link)])
    await a.edit("♻️♻️♻️️️")
    r_subo = []
    r_sub = await get_variable("r_sub", "")
    sub_dict = {}
    for entry in r_sub.strip().split(","):
        if "||" in entry:
            chat_id, invite_link = entry.split("||")
            sub_dict[invite_link] = chat_id

    for invite_link, chat_id in sub_dict.items():
        sada = await get_variable(invite_link, [])
        if user_id not in sada:
            # Check if user is actually in the channel
            try:
                user = await client.get_chat_member(int(chat_id), user_id)
                if user.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT}:
                    r_subo.append(invite_link)
            except UserNotParticipant:
                r_subo.append(invite_link)
            except Exception:
                pass

    for invite_link, chat_id in sub_dict.items():
        if invite_link in r_subo:
            chat = await client.get_chat(int(chat_id))  # Fetch channel details
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"• ᴊᴏɪɴ {chat.title} •",
                        url=invite_link,
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text="• ᴊᴏɪɴᴇᴅ •", callback_data=f"check_subscription{string}"
            )
        ]
    )
    await a.delete()
    text = f"<blockquote>💠 𝙔𝙊𝙊, {message.from_user.mention} ❗️</blockquote>\n\n 𝙔𝙊𝙐 𝙃𝘼𝙑𝙀𝙉'𝙏 𝙅𝙊𝙄𝙉𝙀𝘿 {len(buttons)-1}/{len(FORCE_SUB_CHANNELS)+len(r_subo)} 𝙊𝙁 𝙏𝙃𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇𝙎 𝙍𝙀𝙌𝙐𝙄𝙍𝙀𝘿 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙀 𝘽𝙊𝙏.. ♻️💤\n\n<blockquote>📵 ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ ‼️</blockquote>"
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        message_effect_id=5046509860389126442,
    )


async def check_subscription(client, callback_query: CallbackQuery, string):
    random.choice(images)
    raw_channels = await get_variable(
        "F_sub", "-1002374561133, -1002252580234, -1002359972599"
    )
    FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]
    user_id = callback_query.from_user.id
    not_joined_channels = []
    buttons = []

    for channel in FORCE_SUB_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)
        except Exception as e:
            print(f"{e}")

    r_subo = []
    sub_dict = {}
    for entry in r_sub.strip().split(","):
        if "||" in entry:
            chat_id, invite_link = entry.split("||")
            sub_dict[invite_link] = chat_id

    for invite_link, chat_id in sub_dict.items():
        sada = await get_variable(invite_link, [])
        if user_id not in sada:
            # Check if user is actually in the channel
            try:
                user = await client.get_chat_member(int(chat_id), user_id)
                if user.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT}:
                    r_subo.append(invite_link)
            except UserNotParticipant:
                r_subo.append(invite_link)
            except Exception:
                pass

    if not await not_subscribed(
        1, client, callback_query.message, callback_query.from_user.id
    ):
        new_text = (
            "**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs. ᴛʜᴀɴᴋ ʏᴏᴜ! 😊 /start ɴᴏᴡ**"
        )
        if string:
            new_text = "<blockquote><b><i>Please Click Button Below 👇 to get your file 💠</i></b></blockquote>"
            key = [
                InlineKeyboardButton(
                    text="• ɴᴏᴡ ᴄʟɪᴄᴋ ʜᴇʀᴇ •",
                    url=f"https://t.me/{client.username}?start={string}",
                )
            ]
        else:
            key = None
        if callback_query.message.caption != new_text:
            await callback_query.message.edit_caption(
                caption=new_text,
                reply_markup=InlineKeyboardMarkup([key]) if key else None,
            )

        return

    for invite_link, chat_id in sub_dict.items():
        if invite_link in r_subo:
            chat = await client.get_chat(int(chat_id))
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"• ᴊᴏɪɴ {chat.title} •",
                        url=invite_link,
                    )
                ]
            )

    for channel in not_joined_channels:
        if str(channel).startswith("-100"):  # Private or ID-based channel
            chat = await client.get_chat(channel)
            try:
                # Create a 1-minute expiry invite link
                expire_time = datetime.utcnow() + timedelta(minutes=1)
                invite = await client.create_chat_invite_link(
                    chat_id=channel, expire_date=expire_time
                )
                invite_link = invite.invite_link
            except Exception:
                invite_link = None

            # fallback link if export fails
            link = invite_link or f"https://t.me/c/{channel[4:]}"
            name = chat.title or "Channel"
        else:  # Public channel
            link = f"https://t.me/{channel}"
            name = channel

        buttons.append([InlineKeyboardButton(text=f"• ᴊᴏɪɴ {name} •", url=link)])
    print(f"Not jouned channale ids :- {not_joined_channels}")

    buttons.append(
        [
            InlineKeyboardButton(
                text="• ᴊᴏɪɴᴇᴅ •", callback_data=f"check_subscription{string}"
            )
        ]
    )
    text = f"<blockquote>💠 𝙔𝙊𝙊, {callback_query.from_user.mention} ❗️</blockquote>\n\n 𝙔𝙊𝙐 𝙃𝘼𝙑𝙀𝙉'𝙏 𝙅𝙊𝙄𝙉𝙀𝘿 {len(buttons)-1}/{len(FORCE_SUB_CHANNELS)+len(r_subo)} 𝙊𝙁 𝙏𝙃𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇𝙎 𝙍𝙀𝙌𝙐𝙄𝙍𝙀𝘿 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙀 𝘽𝙊𝙏.. ♻️💤\n\n<blockquote>📵 ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ ‼️</blockquote>"
    await callback_query.answer(
        "Bete I like your smartness But Channel to join karna padega 🪬💀",
        show_alert=True,
    )
    if callback_query.message.caption != text:
        try:
            await callback_query.message.edit_caption(
                caption=text, reply_markup=InlineKeyboardMarkup(buttons)
            )
        except BaseException:
            pass


async def varsa(client, message):
    """
    Handles the /var command to set a variable.
    The command format is: /var variable-name variable-value
    """
    try:
        # Split the message text into parts
        # Split into command and the rest
        parts = message.text.split(maxsplit=1)

        if len(parts) < 2:
            await message.reply_text("Usage: /Vars variable-name - variable-value")
            return

        _, data = parts  # Extract the remaining part after the command

        # Split into variable name and value at the first occurrence of " - "
        if " - " in data:
            variable_name, variable_value = data.split(" - ", 1)
        else:
            await message.reply_text("Usage: /Vars variable-name - variable-value")
            return

        variable_name = variable_name.strip()
        variable_value = variable_value.strip()
        if variable_name == "admin":
            admin = await get_variable("admin", [])
            if not isinstance(admin, list):
                admin = []  # Initialize as an empty list if it's not a list
            try:
                admin_value = int(variable_value)
                admin.append(admin_value)
                await set_variable("admin", admin)
            except ValueError:
                await message.reply_text("Admin value must be an integer.")
                return
        else:
            # Now, you can proceed with handling the variable_name and
            # variable_value

            # Call the set_variable function to store the variable and value
            await set_variable(variable_name, variable_value)
            await message.reply_text(
                f"Variable '{variable_name}' set to '{variable_value}'"
            )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
