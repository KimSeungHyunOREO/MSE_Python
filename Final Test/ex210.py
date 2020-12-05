
def message1(): # 함수 설정
    print("A")

def message2(): # 함수 설정 
    print("B")

def message3(): # 함수 설정
    for i in range (3) : # i 가 2가 될떄까지 돌아간다 = 3번 돌것 
        message2() # B출력
        print("C") # C출력 # 여기까지 for 구문 걸림 
    message1() # 마지막에 A출력

message3()
#따라서 for 구문이 3번 돌아갈 것이므로 BCBCBC가 나오고 마지막에 A가 나올것이다.







# In[ ]:




