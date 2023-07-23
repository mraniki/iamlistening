# """
# Rocket Chat  🚀
# """
# from rocketchat_API.rocketchat import RocketChat

# from iamlistening.config import settings


# async def start_rocket_chat(listener):
#     """Start the RocketChat handler."""

#     rocket = RocketChat(
#         settings.rocket_chat_user,
#         settings.rocket_chat_auth_token,
#         settings.rocket_chat_server
#         )
#     print(rocket.me().json()) 