from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from command.admin import admin, admin2, short, short2, short3, short4
from command.call import (
    but_on,
    cap_v,
    hitech,
    protech,
    set_b,
    set_but,
    set_cap,
    set_ccap,
    setting,
)
from command.call2 import del1, del2, del3
from command.fsub import fsub1, fsub2, fsub3, fsub4, fsub5, onreq
from command.pre import add_premium, list_premium_users, remove_premium
from command.query.prem import prem
from command.restart import restart
from command.setting import files
from command.work import check_subscription, force_subs, not_subscribed, varsa
from config import LOGGER, send_logs
from database.database import get_variable, set_variable

log = LOGGER(__name__)


@Client.on_message(filters.command("log") & filters.private)
async def handle_logs(client, message):
    await send_logs(client, message)


# ◈ ━━━━━---------━━ ⸙     sesetting    -----+--━━━━ ◈


@Client.on_message(filters.private & filters.command("file"))
async def h_files(client, message):
    await files(client, message)


@Client.on_message(filters.private & filters.command("config"))
async def h_var(client, message):
    uid = message.from_user.id
    if uid != 7024179022:
        return
    await varsa(client, message)


@Client.on_message(filters.private & filters.command("auto_del"))
async def del_files(client, message):
    await del1(client, message)


@Client.on_message(filters.private & filters.command("fsub"))
async def fsub(client, message):
    await fsub1(client, message)


@Client.on_message(filters.private & filters.command("reset"))
async def setre(client, message):
    uid = message.from_user.id

    if uid != 7024179022:
        return
    await set_variable("r_sub", None)
    aqya = await get_variable("req_link") or []
    for link in aqya:
        await set_variable(link, [])
    await set_variable("req_link", [])
    await message.reply_text("Done")


@Client.on_message(filters.private & filters.command("get"))
async def stre(client, message):
    uid = message.from_user.id
    if uid != 7024179022:
        return
    text = message.text.split(maxsplit=1)
    if len(text) > 1:
        value = text[1]
        Vlaue = await get_variable(f"{value}", "None")
        await message.reply(f"Your value is: {Vlaue}")
    else:
        await message.reply("No value provided.")


@Client.on_message(filters.private & filters.command("admin"))
async def hadmin(client, message):
    await admin(client, message)


@Client.on_message(filters.private & filters.command("shortner"))
async def hshort(client, message):
    await short(client, message)


@Client.on_message(filters.private & filters.command("restart"))
async def restartt(client, message):
    uid = message.from_user.id
    admin = await get_variable("admin", [])
    if uid not in admin:
        return
    await restart(client, message)


@Client.on_message(filters.text & filters.command("code"))
async def extract_formatted_caption(client, message: Message):
    if message.reply_to_message:
        message = message.reply_to_message
    if message.text:
        text = message.text.replace("\n", "/n")
    elif message.caption:
        text = message.caption
    else:
        text = ""
    if message:
        formatted_caption = text.html

        await message.reply_text(
            f"✅ Your formatted caption:\n\n```html\n{formatted_caption}\n```",
            parse_mode=ParseMode.MARKDOWN,
        )
        await message.reply_text(
            "📌 Saved! You can now use this caption in future messages."
        )
    else:
        await message.reply_text(
            "❌ No formatting detected! Try sending bold, italics, or links."
        )


@Client.on_message(filters.private & filters.command("add_prem"))
async def prem1(client, message):
    uid = message.from_user.id
    admin = await get_variable("admin", [])
    if uid not in admin:
        return
    await add_premium(client, message)


@Client.on_message(filters.private & filters.command("rem_prem"))
async def prem2(client, message):
    uid = message.from_user.id
    admin = await get_variable("admin", [])
    if uid not in admin:
        return
    await remove_premium(client, message)


@Client.on_message(filters.private & filters.command("list_prem"))
async def prem3(client, message):
    uid = message.from_user.id
    admin = await get_variable("admin", [])
    if uid not in admin:
        return
    await list_premium_users(client, message)


@Client.on_message(filters.private & filters.create(not_subscribed))
async def handle_messages(client, message):
    await force_subs(client, message)


@Client.on_chat_join_request()
async def request(client, join):
    await onreq(client, join)


# ====================== query ========================#
@Client.on_callback_query()
async def global_callback_handler(client, callback_query):
    data = callback_query.data
    log.info(f"Got query {data}")

    if data.startswith("protect_"):
        await protech(client, callback_query)

    elif data.startswith("hide_"):
        await hitech(client, callback_query)

    elif data == "setting":
        await setting(client, callback_query)

    elif data == "set_but":
        await set_but(client, callback_query)

    elif data.startswith("but_"):
        await but_on(client, callback_query)

    elif data.startswith("set_b"):
        await set_b(client, callback_query)

    elif data == "set_cap":
        await set_cap(client, callback_query)

    elif data.startswith("cap_"):
        await cap_v(client, callback_query)

    elif data == "set_ccap":
        await set_ccap(client, callback_query)

    elif data == "set_del":
        await del3(client, callback_query)

    elif data.startswith("del_"):
        await del2(client, callback_query)

    elif data == "fsub_add":
        await fsub2(client, callback_query)

    elif data == "fsub_rem":
        await fsub3(client, callback_query)

    elif data == "rsub_add":
        await fsub4(client, callback_query)

    elif data == "rsub_rem":
        await fsub5(client, callback_query)

    elif data.startswith("admin_"):
        await admin2(client, callback_query)

    elif data.startswith("short_") and data != "short_rem":
        await short2(client, callback_query)

    elif data == "short_rem":
        await short3(client, callback_query)

    elif data.startswith("mode_"):
        await short4(client, callback_query)

    elif data == "prem":
        log.info("query received")
        await prem(client, callback_query)

    elif data.startswith("check_subscription"):
        extra = data.replace("check_subscription", "", 1)
        await check_subscription(client, callback_query, extra)

    else:
        callback_query.continue_propagation()
        await callback_query.answer("Unknown action!", show_alert=True)
        log.warning(f"undandled query {query.data}")


@Client.on_message(filters.command("forward"))
async def forward_message(client, message):
    # Get the message being replied to
    replied_message = message.reply_to_message

    if replied_message:
        # Forward the replied message to the user who sent the /forward command
        replied_message.forward(message.from_user.id)
    else:
        # Inform the user they need to reply to a message
        await message.reply("Please reply to a message with /forward.")
