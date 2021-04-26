# discord_bot


## Before start

- Access the Discord's [developer portal](https://discord.com/developers/applications) and login with your discord account.
  **Important**: You’ll need to verify your email before you’re able to move on.
- Create your application selecting `New Application`
- Go to `Bot` tab and click on `Add bot`
- In discord app, create a new server to test your commands
- Back to the [Developer Portal](http://discordapp.com/developers/applications) and select the OAuth2 page from the left-hand navigation
- Scroll down and select _bot_ from the _SCOPES_ options and _Administrator_ from _BOT PERMISSIONS_
- Select _Copy_ beside the URL that was generated for you, paste it into your browser, and select your guild from the dropdown options

## How execute
First, you need to install the dependencies using the command: `pip3 install requirements.txt`

**Important**: recommend use `virtualenv`

- Create a file named `.env` in the same directory as `bot.py`:
```python
# .env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}
```

You’ll need to replace `{your-bot-token}` with your bot’s token, which you can get by going back to the _Bot_ page on the [Developer Portal](http://discordapp.com/developers/applications) and clicking _Copy_ under the _TOKEN_ section

- Start your bot using the following command: 
`python bot.py`

Now you can test the commands in your server.


---
Questions? Access [this tutorial.](https://realpython.com/how-to-make-a-discord-bot-python/)