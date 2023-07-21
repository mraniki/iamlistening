"""
Rocket Chat  🚀
"""
from rocketchat_API.rocketchat import RocketChat

from iamlistening.config import settings


class RockerChatHandler():
    async def start(self):
        # pass
        rocket = RocketChat(
            settings.rocket_chat_user,
            settings.rocket_chat_auth_token,
            settings.rocket_chat_server
            )
        print(rocket.me().json())