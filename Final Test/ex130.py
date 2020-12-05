import requests # request - http 문서를 가져오게 할 수 있는 모듈
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] # 주소에서 자료를 가져옴 

변동폭 = float(btc['max_price']) - float(btc['min_price']) # 정답에 나온 것 처럼 실수가 아닌 정수로해도 결과는 같다. 아마 소수점 단위로 가격이 바뀌어서 그런 것 같다.
시가 = float(btc['opening_price']) # 표에 나온 키 값을 그대로 쓰면 된다.
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가: 
    print("상승장")
else:
    print("하락장")


# In[ ]:



