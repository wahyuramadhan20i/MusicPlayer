# Channel : https://t.me/ruangzeeb


from pyrogram import Client
from config import Config
bot = Client(
    "VCPlayer",
    Config.27275628,
    Config.1f147a7010b1f675e9ed70913224d863,
    bot_token=Config.7853619626:AAGVsY91IcoVkJkNNkPJwNnNntNBpM6m3qk,
    plugins=dict(root="plugins")
)
