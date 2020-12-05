
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2) 
print(c)





# num = 2 이므로 
# 함수2의 num = num + 10에 먼저 들어가서 num = 12가 되고
# 그 12가 함수1로 들어가서 함수0(14) 가 된다
# 함수0(14) 는 28이 되므로 
# 결과는 28이다.

