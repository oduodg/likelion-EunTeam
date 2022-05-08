from pydoc import cli
from urllib import response
import requests
import json

import urllib.request
client_id=""
client_secret=""
encText=urllib.parse.quote("짱구")
url="https://openapi.naver.com/v1/search/movie.json?query="+encText
request=urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response=urllib.request.urlopen(request)
rescode=response.getcode()
if(rescode==200):
    data=json.load(response)
    for i in range(len(data["items"])):

        x= data["items"][i]["title"]
        x=x.replace("<b>","")
        x=x.replace("</b>","")
        print("Title: ",x)
        print("link: ",data["items"][i]["link"])
        y=data["items"][i]["director"]
        if("|" in y):
                y=y.replace("|","")
                print("Director: ",y)
else:
    print("Error Code:"+rescode)