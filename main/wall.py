from main import WALL_API, UNSPLASH_API, session
import aiohttp, random

async def get_wallpapers(query: str):  
  try:
    url = WALL_API + query  
    resp = await session.get(url)
    json = await resp.json()
    images = json["images"]
    if len(images) == 0:
      return "nonee" + "Can't find the wallpaper you are trying to search..."
    random.shuffle(images)
  except Exception as e:
    return "error" + str(e)      
  return images

async def get_unsplash(query: str):  
  try:
    url = UNSPLASH_API + query  
    resp = await session.get(url)
    json = await resp.json()
    images = json["images"]
    if len(images) == 0:
      return "nonee" + "Can't find the wallpaper you are trying to search..."
    random.shuffle(images)
  except Exception as e:
    return "error" + str(e)      
  return images