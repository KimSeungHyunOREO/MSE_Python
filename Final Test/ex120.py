#!/usr/bin/env python
# coding: utf-8

# In[1]:


#120


# In[6]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
Q = input("좋아하는 과일은?") # input으로 답을 받아서
if Q in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.") # 그 대답이 fruit에 있는지 알아내는것


# In[ ]:




