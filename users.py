import json

import pymongo

from bot import Bot  # Import the existing bot instance from bot.py

# Configuration
DB_URI = "mongodb+srv://Mehtadmphta33:Mehtab1234@cluster0.2kwcnnv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "itachi"
CHANNEL_ID = -1002174377932

# MongoDB setup
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database["users"]


def fetch_user_ids():
    try:
        user_docs = user_data.find()
        user_ids = [doc["_id"] for doc in user_docs]
        print(f"Fetched user IDs: {user_ids}")  # Debugging line
        return user_ids
    except Exception as e:
        print(f"Error fetching user IDs: {e}")
        return []


def save_user_ids_to_json(user_ids):
    try:
        with open("Itachi.json", "w") as f:
            json.dump(user_ids, f)
        print("User IDs saved to Itachi.json")
    except Exception as e:
        print(f"Error saving user IDs to JSON file: {e}")


async def send_user_ids_to_channel():
    user_ids = fetch_user_ids()
    if user_ids:
        save_user_ids_to_json(user_ids)

        try:
            async with Bot:
                with open("Itachi.json", "rb") as f:
                    print("Attempting to send document...")
                    response = await Bot.send_document(CHANNEL_ID, f)
                    # Debugging line
                    print(f"Document sent, response: {response}")
            print("User IDs sent to channel successfully.")
        except Exception as e:
            print(f"Error sending file to channel: {e}")
    else:
        print("No user IDs to send.")


async def handle_senduser_command(client, message):
    try:
        await send_user_ids_to_channel()
        await message.reply("User IDs have been successfully sent to the channel.")
    except Exception as e:
        await message.reply(f"Error: {e}")


# Ensure to import this file in your main bot script (bot.py) to register
# the commands.
