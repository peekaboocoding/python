# 학교 축제, 참석률을 높이기 위한 이벤트 진행 
# 댓글 작성자중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰 

# 조건 1) 편의상 댓글은 20명이 작성, 아이디는 1 ~ 20 이라고 가정 
# 조건 2) 댓글 내용과 상관없이 무작위로 추첨하되 중복은 불과 
# 조건 3) random 모듈의 shuffle 과 sample을 활용 


# 출력 예제 
#  -- 당첨자 발표 --
#   치킨 당첨자 : 1
#   커피 당첨자 : [2,3,4]
#  -- 축하합니다 --

from random import * 

users = range(1,21)
users = list(users)


chicken = sample(users,1)
except_coffee = chicken.pop()

users.remove(except_coffee)
coffee = sample(users,3)

print("치킨 당첨자 : {0} \n커피 당첨자 : {1}".format(except_coffee, coffee))
print(" ----------------------------------------------------------------")

shuffle(users)
winners = sample(users,4)
print(winners)
shuffle(winners)
print(winners)
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print(" -- 축하합니다 --")


