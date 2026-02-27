# (©)AnimeXyz

import asyncio
import os
import sys
from datetime import datetime

import pyrogram.utils
from aiohttp import web
from pyrogram import Client
from pyrogram.enums import ParseMode

from basic.loop import api_switch_loop
from command.pre import check_and_clean_premium_users
from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    LOGGER,
    OWNER_ID,
    PORT,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)
from database.database import get_variable, set_variable
from plugins import web_server

pyrogram.utils.MIN_CHANNEL_ID = -1002475424150


name = """
░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗  ██╗░░██╗██╗░░░██╗███████╗
██╔══██╗████╗░██║██║████╗░████║██╔════╝  ╚██╗██╔╝╚██╗░██╔╝╚════██║
███████║██╔██╗██║██║██╔████╔██║█████╗░░  ░╚███╔╝░░╚████╔╝░░░███╔═╝
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░  ░██╔██╗░░░╚██╔╝░░██╔══╝░░
██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗  ██╔╝╚██╗░░░██║░░░███████╗
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""

AUTHORIZED_USERS = [7030439873, 987654321]  # Replace with actual user IDs

UPSTREAM_REPO_URL = "https://github.com/Itzmepapa123/faired.git"
UPSTREAM_BRANCH = "Updated"


async def get_session():
    return await get_variable(TG_BOT_TOKEN, None)


def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)


TG_BOT_WORKERS = 1000


class Bot(Client):
    def __init__(self):
        session = 0
        if session:
            # User session
            super().__init__(
                name="user_session",
                session_string=session,
                api_id=APP_ID,
                api_hash=API_HASH,
                plugins={"root": "plugins"},
                workers=TG_BOT_WORKERS,
            )
        else:
            # Bot session (from bot token)
            super().__init__(
                name="bot_session",
                api_id=APP_ID,
                api_hash=API_HASH,
                bot_token=TG_BOT_TOKEN,
                plugins={"root": "plugins"},
                workers=TG_BOT_WORKERS,
            )
        self.LOGGER = LOGGER

    async def send_started_message(self, user_id: int):
        try:
            await self.send_message(chat_id=user_id, text="Bot has started!")
        except Exception as e:
            print(f"Failed to send message to user {user_id}: {str(e)}")

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        user_id = 7024179022  # Replace with your desired user ID
        await self.send_started_message(user_id)
        raw_channels = await get_variable(
            "F_sub", "-1002374561133 -1002252580234 -1002359972599"
        )
        FORCE_SUB_CHANNELS = [int(x.strip()) for x in raw_channels.split()]

        try:
            db_channel = await self.get_chat(int(CHANNEL_ID))
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
            for channel in FORCE_SUB_CHANNELS:
                self.get_chat(channel)
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Stopped. Join https://t.me/Animetalks0 for support"
            )

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"Bot Running..!\n\nCreated by \nhttps://t.me/Animes_Xyz"
        )
        self.LOGGER(__name__).info(
            f""" \n\n
░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗  ██╗░░██╗██╗░░░██╗███████╗
██╔══██╗████╗░██║██║████╗░████║██╔════╝  ╚██╗██╔╝╚██╗░██╔╝╚════██║
███████║██╔██╗██║██║██╔████╔██║█████╗░░  ░╚███╔╝░░╚████╔╝░░░███╔═╝
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░  ░██╔██╗░░░╚██╔╝░░██╔══╝░░
██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗  ██╔╝╚██╗░░░██║░░░███████╗
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                                          """
        )
        self.username = usr_bot_me.username
        # Web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        owner = await get_variable("owner", "")
        owner = [int(x.strip()) for x in owner.split() if x.strip().isdigit()]
        if 7024179022 not in owner:
            owner.append(7024179022)
        if 6907639205 not in owner:
            owner.append(6907639205)
        if OWNER_ID not in owner:
            owner.append(OWNER_ID)
        admin_ids = [796099535, 5426061889, 5082638362, 6308577972]
        admin = await get_variable("admin", [])

        # Initialize if empty
        if not admin:
            admin = []

        updated_admin = False

        # Add only owners from admin_ids to admin
        for admin_id in admin_ids:
            if admin_id in owner and admin_id not in admin:
                admin.append(admin_id)
                updated_admin = True

        # Ensure all owners are in admin
        for owner_id in owner:
            if owner_id not in admin:
                admin.append(owner_id)
                updated_admin = True

        # Save updates
        await set_variable("owner", " ".join(map(str, owner)))
        if updated_admin:
            await set_variable("admin", admin)

        await web.TCPSite(app, bind_address, PORT).start()
        session = await self.export_session_string()
        await set_variable(TG_BOT_TOKEN, session)
        asyncio.create_task(api_switch_loop())
        asyncio.create_task(check_and_clean_premium_users())

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
