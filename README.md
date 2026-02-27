<!-- Banner -->
<div align="center">

```
███████╗██╗██╗     ███████╗███████╗████████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║██║     ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
█████╗  ██║██║     █████╗  ███████╗   ██║   ██║   ██║██████╔╝█████╗
██╔══╝  ██║██║     ██╔══╝  ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝
██║     ██║██████╗ ███████╗███████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
```

### ⚡ Next-Gen Telegram File Sharing & Monetization Bot ⚡

> 🚀 **Share files. Lock content. Earn money.** — All inside Telegram.
> FileStore is a **lightning-fast** 🔥 bot with built-in Force-Subscribe 🛡️, Ad-Shortener monetization 💰, Premium tiers 💎, auto-deletion ⏳, and a **full admin panel** 👑 — zero coding needed after deploy.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-v2-blueviolet?style=for-the-badge&logo=telegram&logoColor=white)](https://pyrogram.org)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-GPLv3-red?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Itzmepromgitman/FileStore?style=for-the-badge&color=yellow)](https://github.com/Itzmepromgitman/FileStore/stargazers)

</div>

---

## 🧠 What is FileStore?

**FileStore** is a production-ready, fully async Telegram Bot built for high-traffic file distribution. Unlike generic file bots, it ships with:

- 🔥 **uvloop** for a blazing-fast event loop
- 🛡️ **Semaphore-guarded** request handling — no server crashes under load
- 💰 **Monetization-first design** — force users through ad-shorteners or pay for premium

> Built with **Pyrogram v2**, **MongoDB**, **aiohttp**, and love for reliability.

---

## ✨ Feature Showcase

<details open>
<summary><b>🛡️ Force Subscribe System</b></summary>

- **Normal F-Sub**: Requires users to join specified channels before accessing files
- **Request F-Sub (R-Sub)**: Requires users to send a join _request_ (great for private/approval channels)
- Add or remove channels live from within Telegram via the `/fsub` command panel
- Supports multiple channels simultaneously with per-channel join buttons

</details>

<details open>
<summary><b>🔗 Ad-Shortener Monetization</b></summary>

Two powerful modes:

| Mode | How It Works |
|------|-------------|
| **24H Pass** | User watches one ad → unlocked for 24 hours |
| **Per Link** | Every file request requires an ad click |

Premium users **bypass ads entirely**. Set via `/shortner` panel.

</details>

<details open>
<summary><b>⚡ High Performance Architecture</b></summary>

- `uvloop` + `tgcrypto` — **2–4×** faster than standard asyncio
- `GLOBAL_SEMAPHORE(100)` — caps concurrent `/start` executions
- Per-user `asyncio.Lock` — eliminates race conditions
- `flood_safe()` — automatic FloodWait retry with exponential backoff
- Auto-delete & broadcast run as **background tasks** — main coroutine returns instantly

</details>

<details>
<summary><b>👑 Admin Panel & Controls</b></summary>

Everything controlled from within Telegram — no SSH, no config files:

- Add/Remove Admins
- Configure Shortener API, Website and Bypass count
- Toggle Content Protection, Caption Hiding, Auto-Delete timer
- Manage Premium users
- Pull server logs with `/log`
- Hot-restart bot with `/restart`

</details>

<details>
<summary><b>📦 Batch File Delivery</b></summary>

- Encode any range of DB channel messages into a single shareable Base64 link
- Supports 1 file or 100+ files in a single link
- Semaphore-controlled copy loop prevents API spam

</details>

---

## 🏗️ Project Structure

```
FileStore/
│
├── 📄 bot.py              ← Pyrogram Client + startup logic
├── 📄 config.py           ← ENV loading with MongoDB fallback
├── 📄 main.py             ← Entry point
├── 📄 helper_func.py      ← Base64, Shortzy, flood-safe helpers
├── 📄 users.py            ← User management
├── 📄 update.py           ← Auto-update from upstream
│
├── 📁 plugins/
│   ├── start.py           ← /start, file delivery, rate limiting
│   ├── new.py             ← All commands + global callback router
│   ├── link_generator.py  ← Batch link generation
│   ├── channel_post.py    ← Channel post handler
│   └── cbb.py
│
├── 📁 command/
│   ├── admin.py           ← Shortener & admin panel logic
│   ├── fsub.py            ← F-Sub / R-Sub management
│   ├── work.py            ← Subscription verification engine
│   ├── call.py            ← Settings callbacks
│   ├── call2.py           ← Auto-delete callbacks
│   ├── pre.py             ← Premium tier management
│   ├── restart.py         ← Process restart handler
│   └── setting.py         ← /file settings
│
├── 📁 database/
│   └── database.py        ← MongoDB abstraction (get/set variable)
│
└── 📁 basic/
    └── loop.py            ← Background API-switch loop
```

---

## ⚙️ Configuration

### 🔴 Required Variables

| Variable | Description |
|----------|-------------|
| `TG_BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) |
| `APP_ID` | API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | API Hash from [my.telegram.org](https://my.telegram.org) |
| `owner` | Your Telegram User ID (master admin) |
| `CHANNEL_ID` | DB Channel ID (e.g. `-1001234567890`) |
| `DATABASE_URL` | MongoDB connection URI |

### 🟡 Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8080` | Web server port |
| `TG_BOT_WORKERS` | `500` | Worker thread count |
| `START_MSG` | Built-in | Custom HTML welcome message (`{mention}`, `{first}`, `{id}`) |

---

## 📜 Command Reference

```
┌─ USER COMMANDS ────────────────────────────────────────────┐
│  /start          Start the bot or open a shared file link  │
└────────────────────────────────────────────────────────────┘

┌─ ADMIN COMMANDS ───────────────────────────────────────────┐
│  /admin          Master admin management panel             │
│  /shortner       Configure Ad-Shortener settings           │
│  /fsub           Manage Force-Subscribe channels           │
│  /file           File delivery settings                    │
│  /auto_del       Auto-delete timer configuration           │
│  /add_prem       Grant a user Premium access               │
│  /rem_prem       Revoke Premium access                     │
│  /list_prem      List all Premium users                    │
│  /users          Total user count                          │
│  /broadcast      Broadcast message to all users            │
│  /log            Fetch server log file directly in chat    │
│  /restart        Hot-restart the bot process               │
│  /code           Extract HTML caption from a message       │
└────────────────────────────────────────────────────────────┘

┌─ OWNER ONLY ───────────────────────────────────────────────┐
│  /config         Set any DB variable manually              │
│  /get            Read any DB variable value                │
│  /reset          Reset R-Sub tracking data                 │
└────────────────────────────────────────────────────────────┘
```

---

## 🚀 Deployment

### Option 1 — VPS / Local

```bash
# Clone the repository
git clone https://github.com/Itzmepromgitman/FileStore
cd FileStore

# Install requirements
pip3 install -r requirements.txt

# Set ENV variables (or edit config.py)
export TG_BOT_TOKEN="your_bot_token"
export APP_ID="your_app_id"
export API_HASH="your_api_hash"
export owner="your_telegram_id"
export CHANNEL_ID="your_channel_id"
export DATABASE_URL="your_mongodb_uri"

# Start the bot
python3 bot.py
```

### Option 2 — Docker

```bash
docker build -t FileStore .
docker run --env-file .env FileStore
```

### Option 3 — Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

---

## 🔐 Security Checklist

Before going public or deploying, ensure:

- [ ] All ENV variables are set via environment — **no hardcoded tokens in code**
- [ ] Bot is Admin in DB Channel with **Send Messages** permission
- [ ] Bot is Admin in F-Sub channels with **Invite Users via Link** permission
- [ ] MongoDB URI is private and not committed to version control
- [ ] `.gitignore` includes `.env`, `*.session`, and `bot.txt`

---

## 📦 Requirements

```
pyrogram
pyromod
tgcrypto
motor
uvloop
aiohttp
shortzy
```

```bash
pip3 install -r requirements.txt
```

---

## 🙌 Credits & Acknowledgements

| Contributor | Role |
|---|---|
| [Pyrogram](https://github.com/pyrogram/pyrogram) | Core Telegram MTProto framework |
| [pyromod](https://github.com/usernein/pyromod) | Conversational `client.listen()` support |
| [shortzy](https://github.com/theshreyanshpanchal/shortzy) | URL shortener API adapter |
| [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot) | Original inspiration |

---

## 📜 License

Distributed under the **GNU General Public License v3.0**.
See [`LICENSE`](LICENSE) for full details.

---

<div align="center">

**If this project helped you, please drop a ⭐ — it means a lot!**

Made with 🔥 + Python + too much caffeine

</div>
