import requests
import json
import re

headers = {
    'Host' : 'openaip.naver.com',
    'X-Naver-Client-Id' : 'IY6h61h2zaaSoxnd7hO3',
    'X-Naver-Client-Secret': 'AzoelCAY3B',
}

url = 'https://openapi.naver.com/v1/search/movie.json'

params = { 'query' : '태극기 휘날리며',
}

response = requests.get(url,headers = headers, params = params) 
text = eval(response.text)
rem = text["items"][0]["director"]
tit = text["items"][0]["title"]
link = text["items"][0]["link"]

def test(s): 
    hangul = re.compile('[^ ㄱ-ㅣ가-힣+]') 
    result = hangul.sub('', s) 
    return(result)

print(tit)
print(link)
print(rem)
print(rem.strip("|"))
print(test(tit))

