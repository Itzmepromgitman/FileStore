import asyncio
from datetime import datetime, timedelta

import pytz

from database.database import get_variable, set_variable

# Indian timezone
IST = pytz.timezone("Asia/Kolkata")

# Tokens
TOKEN_1 = "20ea608ea708f7caff05fc0c4a7975f702546b5a"
TOKEN_2 = "1f6e13bd296580c5eef0ee253ea2caa48430d2a0"


def time_until_next_trigger(now):
    """
    Returns timedelta until next noon or midnight.
    """
    today = now.date()

    # Today's noon and next midnight
    noon = IST.localize(
        datetime.combine(today, datetime.min.time()) + timedelta(hours=12)
    )
    midnight = IST.localize(
        datetime.combine(today + timedelta(days=1), datetime.min.time())
    )

    return noon - now if now < noon else midnight - now


async def api_switch_loop():
    while True:
        now = datetime.now(IST)
        wait_duration = time_until_next_trigger(now)

        print(f"Sleeping for {wait_duration} until next switch.")
        await asyncio.sleep(wait_duration.total_seconds())

        current_api = await get_variable("api")

        if current_api == TOKEN_1:
            await set_variable("api", TOKEN_2)
        else:
            await set_variable("api", TOKEN_1)


# Start loop (call this from your main async function or bot startup)
# Example: asyncio.create_task(api_switch_loop())
