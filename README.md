#HostCheckerBot (in development)
Telegram bot for check hosts

# Requirements
You must have Python 3 to launch bot.
Also before launching you have to install requirements via pip
```Bash
pip install -r requirements.txt
```
# Configuration
Than you have to create `config.py`:

```Python
# Telegram @OetenBot API Token
TG_TOKEN = '<YOUR_API_KEY>'

# if user_id in this list bot ask user the password:
#       if its correct user can do some more things
ADMIN_LIST = ['<U1_TG_ID>', '<U2_TG_ID>']
ADMIN_PASSWORD = '<ADMIN_PASSWORD>'
```

# Launching

To launch  bot:
```Bash
python ./main.py
```