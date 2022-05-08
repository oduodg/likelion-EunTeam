from base64 import encode
import urllib
import requests

# LG gram 15inch 사용 중, 한글 인코딩 오류 발생으로 추가한 코드입니다.
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
 
url = 'https://openapi.naver.com/v1/search/movie.json'

headers = {
    'Host' : 'openapi.naver.com',
    'X-Naver-Client-Id' : '###',
    'X-Naver-Client-Secret' : '###'
}

params = {
    'query' : '캡틴 아메리카',
}

response = requests.get(url, headers=headers, params=params,) #요청
rescode = response.status_code #요청코드


if(rescode == 200):
    try:
        data = json.loads(response.text) #요청한 data
        for i in range(len(data['items'])):
            title = (data["items"][i]["title"]).replace('<b>','')
            title = title.replace('</b','')
            print('title : ', title)

            link = (data["items"][i]["link"])
            print('link : ', link)

            director = (data["items"][i]["director"]).replace('|','')
            print('directors : ', director, '\n')
    except:
        print("error")