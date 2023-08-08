
======
Config
======

Setting available via settings.toml or .env

.. literalinclude:: ../iamlistening/default_settings.toml


Chat Platform Credentials
=========================


Telegram
--------

- Create your bot token via Telegram @BotFather https://core.telegram.org/bots#how-do-i-create-a-bot 
- Telegram portal to create an API key via https://core.telegram.org/api/obtaining_api_id
- check https://docs.telethon.dev/en/stable/ for more info


Discord
-------

- Create your bot token via Discord Dev Portal https://discord.com/developers/docs/intro
- check https://pycord.readthedocs.io for more info

Matrix
------

- Create your bot token, server, and user via https://app.element.io/#/register
- check https://simple-matrix-bot-lib.readthedocs.io for more info

Guilded
-------

- Create your bot token via Guilded Dev Portal https://support.guilded.gg/hc/en-us/articles/1500009005861-How-to-make-a-bot
- Check https://guildedpy.readthedocs.io/en/stable/

Mastodon
--------

- Create your bot token via Mastodon Dev Portal
- check https://Mastodonpy.readthedocs.io/en/stable/

Lemmy
-----

- Use your user name, user password and lemmy instance url
- check https://github.com/db0/pythorhead

example:

.. code-block:: toml

    VALUE = "On Testing Lemmy"
    chat_platform="lemmy"
    iteration_enabled = true
    iteration_limit = 0
    bot_token = ""
    bot_channel_id = "lemmyworld"
    bot_api_id = ""
    bot_api_hash = ""
    bot_hostname = "https://lemmy.world"
    bot_user = "1234"
    bot_pass = "1234"
    bot_auth_token = ""


Twitch
-----

- Use https://twitchtokengenerator.com to get your bot token
- check https://twitchio.dev/en/latest/ 

example:

.. code-block:: toml

    VALUE = "On Testing Twitch"
    chat_platform="twitch"
    iteration_enabled = true
    iteration_limit = 0
    bot_token = "1233435"
    bot_channel_id = ""
    bot_api_id = ""
    bot_api_hash = ""
    bot_hostname = ""
    bot_user = ""
    bot_pass = ""
    bot_auth_token = ""