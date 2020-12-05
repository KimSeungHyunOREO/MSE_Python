low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]




volatility = [] # 여기에 저장





for i in range(len(low_prices)): # range 그냥 (1,6,1)로 하니까 오류가 나온다 # i가 lowprice의 길이 까지
    volatility.append(high_prices[i] - low_prices[i]) # 변화율은 고가에서 저가 빼면 됨
print(volatility)








# In[ ]:




