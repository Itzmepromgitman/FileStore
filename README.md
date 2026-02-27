<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=7B2FFF&center=true&vCenter=true&width=600&lines=⚡+PowerStorage+Bot;🛡️+Advanced+File+Sharing;🔗+Smart+Monetization;👑+Full+Admin+Control" alt="PowerStorage Bot" />
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pyrogram-2.x-blueviolet?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-Supported-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/Async-First-0088CC?style=for-the-badge&logo=lightning&logoColor=white" />
  <img src="https://img.shields.io/github/license/Itzmepromgitman/powerstorage?style=for-the-badge&color=red" />
</p>

<p align="center">
  <b>A blazing-fast, enterprise-grade Telegram File Sharing Bot with Force-Sub, Ad-Shorteners, Premium Tiers and complete Admin control — all without leaving Telegram.</b>
</p>

---

## 🌟 Why PowerStorage?

> Most file bots are slow, fragile, and lack monetization. **PowerStorage rebuilds from scratch** with uvloop, semaphore-guarded endpoints, per-user async locks, and flood-safe retry loops — so you never lose a user to a timeout.

---

## ✨ Feature Highlights

| Feature | Description |
|---|---|
| ⚡ **High Performance** | `uvloop` + `tgcrypto` — 2–4× faster TLS & event loop |
| 🛡️ **Dual Force-Subscribe** | Normal F-Sub AND Request-only R-Sub channels |
| 🔗 **Ad Shortener System** | 24-Hour Pass Mode or Per-Link Mode via Shortzy |
| 👑 **Dynamic Admin Panel** | Full control from within Telegram — no SSH needed |
| 💎 **Premium Tiers** | Grant users shortener bypass and special access |
| 🗑️ **Auto-Deletion** | Schedule file removal with a custom countdown timer |
| 📦 **Batch Links** | Deliver multiple files with a single encoded link |
| 🔒 **Content Protection** | Optional `protect_content` flag on all shared media |
| 💬 **Custom Captions** | Use HTML templates with dynamic file name/caption fills |
| 🌐 **Web Server** | Built-in `aiohttp` server for health checks & keep-alive |
| 📄 **Remote Log Access** | Pull server logs via `/log` — no console required |
| 🔁 **Hot Restart** | `/restart` reloads the bot process without a server reboot |

---

## 🏗️ Architecture

```
powerstorage/
├── bot.py              ← Pyrogram Client bootstrap & startup hooks
├── config.py           ← ENV loading with DB-backed fallbacks
├── main.py             ← Entry point
├── helper_func.py      ← Base64 encode/decode, Shortzy wrapper, flood-safe helpers
├── users.py            ← User management helpers
├── update.py           ← Auto-update from upstream repo
│
├── plugins/
│   ├── start.py        ← Core /start handler, file delivery, rate-limiting
│   ├── new.py          ← Command + global callback query router
│   ├── link_generator.py
│   ├── channel_post.py
│   └── cbb.py
│
├── command/
│   ├── admin.py        ← Shortener config & admin management
│   ├── fsub.py         ← F-Sub & R-Sub add/remove logic
│   ├── work.py         ← Subscription verification engine
│   ├── call.py         ← Settings callbacks (protect, caption, button, etc.)
│   ├── call2.py        ← Auto-delete callbacks
│   ├── pre.py          ← Premium user add/remove/list & cleanup loop
│   ├── restart.py      ← Graceful process restart
│   └── setting.py      ← /file command handler
│
├── database/
│   └── database.py     ← MongoDB get/set abstraction layer
│
└── basic/
    └── loop.py         ← Background API-switch loop task
```

---

## ⚙️ Environment Variables

Set these in your system environment **OR** pass them to your hosting platform.

### 🔴 Required

| Variable | Description |
|---|---|
| `TG_BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) |
| `APP_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `owner` | Your Telegram User ID (master admin) |
| `CHANNEL_ID` | DB Channel ID where files are stored (e.g. `-100xxxxxxxxxx`) |
| `DATABASE_URL` | MongoDB connection URI |

### 🟡 Optional

| Variable | Default | Description |
|---|---|---|
| `PORT` | `8080` | Web server port |
| `TG_BOT_WORKERS` | `500` | Async worker thread count |
| `START_MSG` | Built-in | Custom HTML welcome message |

---

## 🤖 Bot Commands

```
/start         →  Start the bot or decode & deliver a file link
/admin         →  Open the Admin management panel
/shortner      →  Configure Ad-Shortener website, API & mode
/fsub          →  Manage Force-Subscribe & Request-Subscribe channels
/file          →  View file delivery settings
/auto_del      →  Configure auto-deletion timer for shared files
/add_prem      →  Grant a user Premium access
/rem_prem      →  Revoke a user's Premium access
/list_prem     →  List all current Premium users
/users         →  Total user count
/broadcast     →  Send a message to all bot users
/log           →  Fetch server log file directly in chat
/restart       →  Hot-restart the bot process
/code          →  Extract HTML-formatted caption from a message
/get           →  [Owner] Read any DB variable value
/config        →  [Owner] Write any DB variable value
/reset         →  [Owner] Reset R-Sub invite link tracking
```

---

## 💡 How Shortener Modes Work

```
[ 24H MODE ]
User visits link → Must watch ad → Receives 24-hr pass → Downloads file freely
Premium users → Skip instantly with no ad 🎉

[ PER-LINK MODE ]
User gets a locked link button → Clicks ad-shortener link → Receives unlock link
Premium users → Direct unlock link, zero ads 🎉
```

---

## 🚀 Deployment

### Local / VPS

```bash
git clone https://github.com/Itzmepromgitman/powerstorage
cd powerstorage
pip3 install -r requirements.txt
# Set your ENV variables (export or .env)
python3 bot.py
```

### Docker

```bash
docker build -t powerstorage .
docker run --env-file .env powerstorage
```

### Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

---

## 🔐 Security Notes

- ⚠️ **Never hardcode** tokens or API hashes directly in `config.py`. Always use ENV variables.
- 🛡️ Force-Subscribe channels must have the bot added as an **Admin with Invite Links permission**.
- 🔒 The DB Channel must have the bot added as an **Admin with Send Messages permission**.
- 🌐 Only the `OWNER_ID` and added admins can access sensitive bot commands.

---

## 📦 Dependencies

```
pyrogram
pyromod
tgcrypto
motor
uvloop
aiohttp
shortzy
```

Install via:
```bash
pip3 install -r requirements.txt
```

---

## 🙌 Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram) — the heart of this bot
- [pyromod](https://github.com/usernein/pyromod) — conversational listeners
- [Shortzy](https://github.com/theshreyanshpanchal/shortzy) — URL shortener adapter
- Original inspiration: [CodeXBotz/File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)

---

## 📜 License

This project is licensed under the **GNU GPLv3**.
See [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>⭐ Star this repo if it helped you! ⭐</b><br/>
  Made with 💜 using Python & Pyrogram
</p>
