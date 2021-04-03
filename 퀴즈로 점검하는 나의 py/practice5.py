# 50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램 작성 

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수를 정해짐
# 조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 함. 

# (출력문 예제)

import random
import sys



cnt = 0
for i in range(50):
    man = i+1
    time = random.randint(5,50)
    if time >= 5 and time < 16 :
        #print('[O] '+ str(man)+ '번째 손님 (소요시간 : '+ str(time) +'분)')
        print('[O] {0} 번째 손님 (소요시간 : {1}분)'.format(man, time))
        cnt=cnt+1
    else :
        print('[ ] {0} 번째 손님 (소요시간 : {1}분)'.format(man, time))

print('총 탑승 승객 : ' +str(cnt) +'분')
    