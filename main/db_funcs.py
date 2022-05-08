from main import db
from bson.objectid import ObjectId

imagesdb = db.images

async def get_image(id): 
  data = await imagesdb.find_one({"_id": ObjectId(id)})
  image_url = data["image"]
  return image_url

async def save_image(url): 
  data = await imagesdb.insert_one({"image": url})
  id = data.inserted_id
  return str(id)
  
async def del_image(id): 
  data = await imagesdb.delete_one({"_id": ObjectId(id)})
  return