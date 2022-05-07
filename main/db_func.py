from main import db

imagesdb = db.images

async def get_image(id): 
  data = await imagesdb.find_one({"_id": id})
  image_url = data["image"]
  return image_url

async def save_image(url): 
  data = await imagesdb.insert_one({"image": url})
  id = data["_id"]
  return id
  
async def del_image(id): 
  data = await imagesdb.delete_one({"_id": id})
  return