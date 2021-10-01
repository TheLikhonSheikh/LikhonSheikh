from pyrogram import filters

from wbb import app
from wbb.core.decorators.errors import capture_err
from wbb.core.keyboard import ikb
from wbb.core.sections import section
from wbb.utils.http import get

__MODULE__ = "price"
__HELP__ = """
/token
        Get Real Time value from currency given.
"""


@app.on_message(filters.command("price"))
@capture_err
async def token(_, message):
    if len(message.command) < 2:

    currency = message.text.split(None, 1)[1].lower()

    btn = ikb(
        {"Support": "https://t.me/GodFatherMob"},
    )

    m = await message.reply("`Processing...`")

    import requests

data = requests.get("https://api.pancakeswap.info/api/v2/tokens/0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3").json()

print(data["data"]["price"])
