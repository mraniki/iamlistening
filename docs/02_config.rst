
======
Config
======

Setting available via settings.toml or .env

.. literalinclude:: ../iamlistening/default_settings.toml


Chat Platform Credentials
=========================


Telegram
--------

- Create your bot token via Telegram @BotFather 
- Telegram portal to create an API key


Discord
-------

- Create your bot token via Discord Dev Portal

Matrix
------

- Create your bot token, server, and user via Matrix Dev Portal

Guilded
-------

- Create your bot token via Guilded Dev Portal

Mastodon
--------

- Create your bot token via Mastodon Dev Portal

Lemmy
-----

- Use the your user name, user passworld and lemmy instance url

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