from pyrogram import filters

from wbb import app
from wbb.core.decorators.errors import capture_err
from wbb.core.keyboard import ikb
from wbb.core.sections import section
from wbb.utils.http import get

__MODULE__ = "Price"
__HELP__ = """
/price [currency]
        Get Real Time value from currency given.
"""


@app.on_message(filters.command("price"))
@capture_err
async def price(_, message):
    if len(message.command) < 2:
        return await message.reply("/price [currency]")

    currency = message.text.split(None, 1)[1].lower()

    btn = ikb(
        {"Available Currencies": "https://t.me/likhonsupport/5"},
    )

    m = await message.reply("`Processing...`")

    try:
        r = await get(
            "https://api.pancakeswap.info/api/v2/tokens",
            timeout=5,
        )
    except Exception:
        return await m.edit("[ERROR]: Something went wrong.")

    if currency not in r:
        return await m.edit(
            "[ERROR]: INVALID CURRENCY",
            reply_markup=btn,
        )

    body = {i.upper(): j for i, j in r.get(currency).items()}

    text = section(
        "Current Crypto Rates For " + currency.upper(),
        body,
    )
    await m.edit(text, reply_markup=btn)
