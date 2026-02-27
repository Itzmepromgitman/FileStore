<blockquote><h1 align="center">✨ 𝐏𝐨𝐰𝐞𝐫𝐒𝐭𝐨𝐫𝐚𝐠𝐞 - 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐅𝐢𝐥𝐞 𝐁𝐨𝐭 ✨</h1></blockquote>

<blockquote><p align="center">
  <img src="https://img.shields.io/badge/Made_with-Python-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-Pyrogram-blueviolet?style=for-the-badge&logo=telegram" />
</p></blockquote>

<blockquote>📜 <b>𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄</b>
PowerStorage is an aggressively optimized, async-first File Sharing & Link Generation Bot for Telegram. Tailor-made for administrators and channel owners who want deep insights, comprehensive force-subscription layers (F-Sub & R-Sub), and direct monetization interfaces via shorteners. 🚀</blockquote>

<blockquote>⭐️ <b>𝗞𝗲𝘆 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀</b>

• ⚡ <b>𝗛𝗶𝗴𝗵 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲:</b> Integrated `uvloop` & `tgcrypto` to handle thousands of requests seamlessly.
• 🛡 <b>𝗦𝗺𝗮𝗿𝘁 𝗙𝗼𝗿𝗰𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻𝘀 (𝗙-𝗦𝘂𝗯/𝗥-𝗦𝘂𝗯):</b> Require users to join public channels (F-Sub) or process join-requests (R-Sub) effortlessly.
• 🔗 <b>𝗕𝘂𝗶𝗹𝘁-𝗶𝗻 𝗠𝗼𝗻𝗲𝘁𝗶𝘇𝗮𝘁𝗶𝗼𝗻:</b> Fully baked Shortzy API integration. Admins can lock files behind 24-hr Shortener Passes or Per-Link bypasses.
• 👑 <b>𝗗𝘆𝗻𝗮𝗺𝗶𝗰 𝗔𝗱𝗺𝗶𝗻 𝗣𝗮𝗻𝗲𝗹:</b> Control API keys, bot behavior, F-Sub lists, and user premium tiers entirely from within Telegram via `/admin`.
• 📦 <b>𝗦𝗲𝗰𝘂𝗿𝗲 𝗕𝗮𝘁𝗰𝗵𝗶𝗻𝗴:</b> Generates encrypted Base64 strings to safeguard stored content indices.
</blockquote>

<blockquote>⚙️ <b>𝗘𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀</b>
Ensure you populate your `config.py` (or system ENV) with the following required vars:

* `TG_BOT_TOKEN`: The bot token acquired from @BotFather
* `APP_ID`: Telegram API ID from my.telegram.org
* `API_HASH`: Telegram API Hash
* `OWNER_ID`: Your personal Telegram User ID (Grants master admin rights)
* `CHANNEL_ID`: The Database Channel ID where files originate (e.g., `-100xxxxxxx`)
* `PORT`: Server port (default 8080)
</blockquote>

<blockquote>🛠️ <b>𝗕𝗼𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>

<b>➪ /start :</b> Initializes bot or decrypts links.
<b>➪ /admin :</b> Opens the master configuration panel.
<b>➪ /shortner :</b> Manage website shorteners, APIs, & Bypass modes.
<b>➪ /fsub :</b> Open the interactive settings for F-Sub and R-Sub channels.
<b>➪ /users :</b> See live user statistics.
<b>➪ /broadcast :</b> Mass-reply announcement to all users.
<b>➪ /log :</b> Pull `bot.txt` (server logs) natively through chat!
</blockquote>

<blockquote>🚀 <b>𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁</b>

<b>𝗟𝗼𝗰𝗮𝗹𝗹𝘆 / 𝗩𝗣𝗦:</b>
```bash
git clone <your-repo>
cd powerstorage
pip3 install -r requirements.txt
# Populate config.py ENV here
python3 bot.py
```
</blockquote>

<blockquote>🛑 <b>𝗗𝗶𝘀𝗰𝗹𝗮𝗶𝗺𝗲𝗿</b>
Ensure you keep your ENV Variables extremely private! This project relies on MongoDB (in database implementations) and Pyrogram for Telegram connection.
Happy Sharing! 🎉</blockquote>
