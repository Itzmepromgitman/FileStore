import asyncio
import logging
import os
import random
from logging.handlers import RotatingFileHandler

from database.database import set_variable

images = [
    "https://i.postimg.cc/RVD4RpG1/1329839.jpg",
    "https://i.postimg.cc/G3MCLS00/1329845.jpg",
    "https://i.postimg.cc/NFPqdL8G/1329915.jpg",
    "https://i.postimg.cc/yYBvG7ps/1332278.jpg",
    "https://i.postimg.cc/NfHBd7nW/1343620.png",
    "https://i.postimg.cc/TYqH2K5K/1343746.png",
    "https://i.postimg.cc/h4m5wySb/1343747.png",
    "https://i.postimg.cc/fThrhcy4/1362335.jpg",
    "https://i.postimg.cc/j52rPzN3/1363139.png",
    "https://i.postimg.cc/wM5FBrvC/545909.jpg",
    "https://i.postimg.cc/BQgM9RRD/599379.jpg",
    "https://i.postimg.cc/Kj1svfLF/740666.png",
    "https://i.postimg.cc/7YmMQ0Tn/749966.png",
    "https://i.postimg.cc/t70DRjpt/928887.jpg",
    "https://i.postimg.cc/qRD45m4d/goku-ultra-instinct-5120x2880-21414.png",
    "https://i.postimg.cc/yYgYwzDp/luffy-straw-hat-3840x2160-20824.png",
]

img = random.choice(images)

ADMINS = []


def get_variable_sync(var_name, default=None, datatype=str):
    # Corre.ctly get from os..environ
    value = os.environ.get(var_name)
    if value is None:
        return datatype(default)
    try:
        return datatype(value)
    except (ValueError, TypeError):
        return default


async def set_variable_async(var_name, data):
    await set_variable(var_name, data)


def get_env(var_name, data=None, datatype=str):
    """
    Gets the variable from ENV.
    If missing, set it to provided data using set_variable().
    """
    value = os.environ.get(var_name)
    if value is None:

        try:
            asyncio.get_event_loop().run_until_complete(
                set_variable_async(var_name, data)
            )
        except RuntimeError:
            asyncio.run(set_variable_async(var_name, data))
        return datatype(data)  # Safely return the provided default value
    else:
        try:
            return datatype(value)
        except (ValueError, TypeError):
            return data


# Example Usage:


# ======================
# Now your config below is fully sync:
# ======================
TG_BOT_TOKEN = get_env("TG_BOT_TOKEN", "")
APP_ID = get_env("APP_ID", "", int)
API_HASH = get_env("API_HASH", "")
OWNER_ID = get_env("owner", "", int)
CHANNEL_ID = get_env("CHANNEL_ID", "", int)
PORT = get_env("PORT", "8080")
TG_BOT_WORKERS = int(get_env("TG_BOT_WORKERS", "500", int))
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"
premiumurl="https://t.me/Powerprime_plans/12"
# ======================
# Logging
# ======================
LOG_FILE_NAME = "bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


async def send_logs(client, message):
    log_file = "bot.txt"

    if os.path.exists(log_file):
        with open(log_file, "rb") as f:
            await message.reply_document(f, caption="📄 Here are the latest logs.")
    else:
        await message.reply_text("⚠️ No logs found.")

