import urllib.request
import json

client_ID = "xjWt8iT0npl6jyAv7FdX"
client_Secret = "ltEcwYiR8H"

encText = urllib.parse.quote("스파이더맨")

url = "https://openapi.naver.com/v1/search/movie.json?query=" +encText

request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id", client_ID)
request.add_header("X-Naver-Client-Secret", client_Secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if (rescode == 200):
    response_body = json.load(response)
    
    x = response_body["items"][0]["title"]
    x = x.replace('<b>', '')
    x = x.replace('</b>', '')
    print("제목: ", x)
    
    print(response_body["items"][0]["link"])
    
    y = response_body["items"][0]["director"]
    y = y.replace ('|', '')
    print("감독: ", y)

    z = response_body["items"][0]["actor"]
    z = z.replace ('|', '')
    print("배우: ", z)
    
    # print(response_body)


else:
    print("Error Code:" + rescode)

