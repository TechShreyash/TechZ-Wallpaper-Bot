from main import app
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from main.sel import scrap_mkv


@app.on_message(filters.command("start") & filters.private & filters.user([1689542319, 1693701096]))
async def start(bot, message: Message):
    await message.reply_text('Online...')


@app.on_message(filters.command("scrap") & filters.private & filters.user([1689542319, 1693701096]))
async def help(bot, message: Message):
    try:
        msg = await message.reply_text('Processing...')
        await scrap_mkv(message.text.split(' ')[1], msg)
    except Exception as e:
        await message.reply_text(f'Error : {str(e)}')


if __name__ == "__main__":
    print("==================================")
    print("[INFO]: BOT STARTED BOT SUCCESSFULLY")
    print("==========JOIN @TECHZBOTS=========")

    idle()
    print("[INFO]: BOT STOPPED")
