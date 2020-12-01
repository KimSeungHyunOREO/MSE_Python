#!/usr/bin/env python
# coding: utf-8

# In[1]:


#110


# In[2]:


if True : # 참으로 시작 했으므로
    if False:
        print("1")
        print("2")
    else:
        print("3") 
else :
    print("4")
print("5")


# In[3]:


#if True : # 참으로 시작 했으므로
# ... 
#else :
    #print("4") # 여기 부분은 필요가 없다 참이 아닐 때 니까


# In[4]:


#if False: # 여기서 만약에 거짓이면을 가정하고 있음 # 하지만 우리는 참 값을 출력 할 것이니까 1,2 는 건너뛰게됨
    #print("1")
    #print("2")
#else: # 여기가 출력되니까 3이 살아남고
    #print("3") 


# In[5]:


#print("5") 이 부분은 if문과 관련이 없으니까 5가 출력된다


# In[ ]:


# 따라서 3과 5가 출력된다.

