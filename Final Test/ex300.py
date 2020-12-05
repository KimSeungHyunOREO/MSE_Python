#
try:
    #실행 코드
except:
    #예외가 발생했을 때 수행할 코드
else:
    #예외가 발생하지 않았을 때 수행할 코드
finally:
    #예외 발생 여부와 상관없이 항상 수행할 코드





per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except: # 실수로 변환이 안되므로 예외생김
        print(0)
    else: # 예외가 없다면
        print("clean data")
    finally: # 예외는 상관없이 무조건 실행
        print("변 환 완 료")




# 10.31은 문제가 없으니까 clean data 와 변환완료
# "" 공백은 실수 변환이 안되니까 0과 변환완료
# 8.00은 문제가 없으니까 clean data 와 변환완료
# 가 출력 될 것이다.

