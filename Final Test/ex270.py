#!/usr/bin/env python
# coding: utf-8

# In[1]:


#270


# In[8]:


종목 = [] # 리스트를 만들고

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) # 클래스를 만들고
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37) 

종목.append(삼성) # 추가를 해준다
종목.append(현대차)
종목.append(LG전자)

for i in 종목: # 이제 출력
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문


# In[ ]:



