import aiohttp
from pyrogram import Client
from config import *
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("[INFO]: STARTING BOT...")
app.start()

print("[INFO]: STARTING AIOHTTP CLIENT")
session = aiohttp.ClientSession()

print("[INFO]: STARTING MONGO DB CLIENT")
mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client.walldb