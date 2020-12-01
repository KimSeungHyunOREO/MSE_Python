#!/usr/bin/env python
# coding: utf-8

# In[1]:


#200


# In[3]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100], # 1일차
        [200, 210, 180, 190], # 2일차
        [300, 310, 300, 310]] # 3일차


# In[ ]:





# In[10]:


total = 0 # 전체 이익 초기값
for daily in ohlc[1:]: # 첫 줄 건너뜀
    profit = (daily[3] - daily[0]) #  시작할때 사서 닫을때 팔것이므로 수익은 둘을 빼주면 된다.
    total += profit # 매일매일 적립 
print(total)


# In[ ]:




