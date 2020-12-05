
class 부모: # 클래스 
  def __init__(self): # 생성자
    print("부모생성") 

class 자식(부모): # 상속받음
  def __init__(self): # 생성자 호출 
    print("자식생성") 
    super().__init__() # 부모클래스에 접근가능 # self 전달

나 = 자식() # 객체생성


# In[3]:


#1. #나 = 자식() # 객체생성
#2. class 자식(부모): # 상속받음
  #def __init__(self): # 생성자 호출 
    #print("자식생성")
#3. super().__init__() # 부모클래스에 접근가능 # self 전달
#4. class 부모: # 클래스 
  #def __init__(self): # 생성자
    #print("부모생성") 


# In[ ]:


# 따라서 자식생성 부모생성 순으로 출력 될 것이다.

