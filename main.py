from fastapi import FastAPI
from pydantic import BaseModel
import requests
import pandas as pd
from PIL import Image
import io
import os 
import urllib
import importlib
Image_Similarity=importlib.import_module("Image_Similarity")
class Input (BaseModel):
    url: str
app = FastAPI()

@app.post("/getLink/")
def getImage(input: Input):
    filename=input.url.split("/")[-1]
    req=urllib.request.Request(input.url,headers={"User-Agent":"Mozilla/5.0"})
    im=urllib.request.urlopen(req).read()
    path=filename
    img= Image.open(io.BytesIO(im))
    img.save(path)
    similar_images_dict=Image_Similarity.SearchImage().get_similar_images(image_path=Image_Similarity.image_list[0],number_of_images=10)
    url_prefix="https://www.valentino.com/"
    pred={}
    for index in similar_images_dict :
        image_path=similar_images_dict[index].split("/")
        image_path=image_path[-1].split("-")
        image_path=url_prefix+image_path[0]+"/"+image_path[-1]
        pred[index]=image_path
    os.remove(path)
    return pred