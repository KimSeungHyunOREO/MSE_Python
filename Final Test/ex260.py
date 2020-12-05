# 여기부터 좀 어려워지네
class OMG : 
    def print() :
        print("Oh my god")
mystock = OMG()
mystock.print() # OMG.print(mystock) # mystock 변수안에 프린트가 없음


# In[ ]:


# OMG안에 print가 있음
# 그 print는 함수를 바인딩함 (함수가 따로 있음)
# mystock 변수 생김
# mystock 변수안에 프린트가 없음
# 그래서 함수를 호출함
# (.)객체로 호출하면  # OMG.print(mystock) 이렇게 호출됨

