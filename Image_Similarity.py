import pandas as pd
import pandas as pd
import requests
from PIL import Image
import io
import os 
import urllib
from wsgiref import headers

import DeepImageSearch
from DeepImageSearch import Index , LoadData, SearchImage

df=pd.read_csv("image-similarity-bc0atzhw1x-valentino_images.csv")

def getLink(filename):
    res=df.loc[df['image'].str.contains(filename, case=False)]
    return res.iloc[0,0]

if os.path.exists("Data"):
    image_list= LoadData().from_folder(["Data"])
    Index(image_list).Start()
else:
    os.mkdir("Data")
    

    for line in df["image"]: 
        
        filename=line.split("/")[-1]
        
        path=os.path.join("./Data/",filename)
        URL=line
        req=urllib.request.Request(URL,headers={"User-Agent":"Mozilla/5.0"})
        im=urllib.request.urlopen(req).read()
        
        img= Image.open(io.BytesIO(im))
        img.save(path)

    image_list= LoadData().from_folder(["Data"])
    Index(image_list).Start()