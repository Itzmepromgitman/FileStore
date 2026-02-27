import pymongo

from data import DB_NAME, DB_URI

# Initialize MongoDB client
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database["users"]
config_data = database["config"]


async def add_user(user_id: int):
    try:
        user_data.insert_one({"_id": user_id})
    except Exception as e:
        print(f"Error adding user {user_id}: {e}")


async def present_user(user_id: int):
    try:
        found = user_data.find_one({"_id": user_id})
        return bool(found)
    except Exception as e:
        print(f"Error finding user {user_id}: {e}")
        return False


async def full_userbase():
    try:
        user_docs = user_data.find()
        user_ids = [doc["_id"] for doc in user_docs]
        return user_ids
    except Exception as e:
        print(f"Error retrieving user base: {e}")
        return []


async def del_user(user_id: int):
    try:
        result = user_data.delete_one({"_id": user_id})

    except Exception as e:
        print(f"Error deleting user {user_id}: {e}")


async def set_variable(key: str, value):
    """Set a configuration variable in the database."""
    config_data.update_one(
        {"_id": key},
        {"$set": {"value": value}},  # Stores value directly, preserving type
        upsert=True,
    )


async def get_variable(key: str, default=None):
    """Retrieve a configuration variable from the database and fallback to default if missing or None."""

    if config_data is None:
        raise Exception("config_data collection is not initialized!")

    entry = config_data.find_one({"_id": key})
    if not entry:
        # Insert the key with default value (can be None or an actual default)
        config_data.insert_one({"_id": key, "value": default})
        return default

    value = entry.get("value", default)
    # Handle case when the value is None
    if value is None:
        return default
    return value


async def get_all_variables():
    """Retrieve all configuration variable keys and values from the database."""
    cursor = config_data.find({})
    variables = []
    async for entry in cursor:
        variables.append((entry["_id"], entry["value"]))
    return variables
