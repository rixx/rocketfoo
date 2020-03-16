import json

from rocketchat_API.rocketchat import RocketChat


if __name__ == "__main__":
    credentials = json.load("credentials.json")
    rocket = RocketChat(
        auth_token=credentials["token"],
        user_id=credentials["user_id"],
        server_url=credentials["domain"],
    )
    rocket.chat_post_message("test", channel="bottest")
