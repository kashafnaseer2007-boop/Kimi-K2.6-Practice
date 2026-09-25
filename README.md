# 🧠 Kimi K2.6 Chat (Local)

A simple chat app to run **Kimi K2.6** on your own computer using a free API key from [Fireworks AI](https://fireworks.ai).

![Preview](https://img.shields.io/badge/works-on%20your%20PC-brightgreen)

## What you need

- Windows (this guide)
- Python installed ([python.org](https://python.org))
- A free account at [Fireworks AI](https://fireworks.ai)

## Quick start (5 minutes)

### 1. Get a free API key
- Go to [fireworks.ai](https://fireworks.ai) and sign up
- After login, go to **API Keys** and create a new key
- Copy the key (starts with `fw_`)

### 2. Download or copy these 3 files

Save them in a folder named `Kimi_Practice`:

**`app.py`** – the main program
**`index.html`** – the chat interface
**`requirements.txt`** – list of packages

> If you don't have `index.html`, just create an empty file – the app will still work.

### 3. Install and run

Open **Command Prompt** (cmd) inside your `Kimi_Practice` folder, then run:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Now set your API key:

```cmd
set FIREWORKS_API_KEY=fw_your_key_here
```

And finally:

```cmd
python app.py
```

### 4. Use it

Open your browser and go to:  
➡️ **http://127.0.0.1:7860** ⬅️

Type a message and press Enter. That's it!

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Connection error` | Restart your computer and run again |
| `Missing credentials` | You forgot to set `set FIREWORKS_API_KEY=...` |
| `403 error` | Your key is wrong or expired – get a new one from Fireworks |

## Need to change the code to use Fireworks?

If your `app.py` still uses Hugging Face, change **only these lines**:

```python
client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.environ.get("FIREWORKS_API_KEY", ""),
)
```

And the model name to:

```python
model="accounts/fireworks/models/kimi-k2p6",
```

Then save and run again.

---

Made with ☕ and Python for developers who just want things to be done.