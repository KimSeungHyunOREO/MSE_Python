#!/usr/bin/env python
# coding: utf-8

# In[1]:


#50


# In[2]:


data = "039490     "
print(data) # 출력해보면 공백이 있는지 잘 모름


# In[4]:


data1 = data.strip() # 1번
print(data1) 


# In[6]:


data = data.rstrip() # 2번
print(data)


# In[7]:


# 1번과 2번의 결과값이 같은 것 같다.
# 2번의 r은 right 라는 의미로 오른쪽 공백을 지워 준다.


# In[ ]:




