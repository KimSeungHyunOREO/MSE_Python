#!/usr/bin/env python
# coding: utf-8

# In[24]:


#160


# In[ ]:


# 내가 해보다가 인터넷 자료 참고해서 만든 답 # 참고: https://daeunginfo.blogspot.com/2019/04/python_15.html


# In[14]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']


# In[29]:


search_1 = '.h' # 찾는 것 설정


# In[30]:


h_list = list() # 리스트 값으로 받을 예정
for i in 리스트:
    if search_1 in i:
        h_list.append(i) # 추가!


# In[31]:


search_2 = '.c'


# In[32]:


c_list = list()
for j in 리스트:
    if search_2 in j:
        c_list.append(j)


# In[33]:


print(h_list, c_list)


# In[38]:


# or로 묶어서 한번에 출력해보려 했는데..


# In[40]:


# 여기부턴 정답에 있던거


# In[34]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".") # .c .h를 찾는거여서 .단위로 쪼갬
  if (split[1] == "h") or (split[1] == "c"): # 그리고 h와 c랑 같은것을 찾아서
    print(변수) # 변수 출력


# In[ ]:




