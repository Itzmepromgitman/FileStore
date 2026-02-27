import os
import sys


async def restart(client, message):
    await message.reply_text("Updating and restarting bot...")

    try:
        exit_code = os.system("python3 update.py")

        if exit_code == 0:
            await message.reply_text("✅ Update successful! Restarting bot...")
        else:
            await message.reply_text("⚠️ Update failed! Restarting bot anyway...")

        # Restart the bot process
        os.execv(sys.executable, ["python3", "main.py"])
    except Exception as e:
        print(f"ERROR:-{str(e)}")
