def func():
    print("함수")

balance = 1000

# 전달값 과 반환값

def withdraw_night (balance, money):
    commission = 100
    return commission  , balance - money - commission

commision, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다".format(commision, balance))
    
# 기본 값 

def profile(name, age=5):
    print("이름 : {0}, 나이 : {1}".format(name, age))

profile('박범수')
profile('우진영','30')

# 가변함수 
# 함수 이름은 profile, 가변함수를 이용해서 사용할 수 있는 언어를 넣을 수 있는 함수 만들기 

def profile(name, *langs):
    print("이름 : {0}".format(name), end= '\t')
    for lang in langs:
        print(lang, end=' ')
    print()

profile('박범수','java','c','c++','kotlin')


