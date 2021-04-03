import sys
# https://youtu.be/kWiCuklohdY?t=10753 

# 표준 입출력 

# 정렬
scores = {"수학" : 0 , "영어" : 100, "코딩" : "53"}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

sys.exit()

# 숫자 0으로 채우기 
for num in range(5):
    print("대기번호 : {0}".format(str(num).zfill(3)))

# 입력값
answer = input("값을 입력하세요")
print("입력하신 값은 {0} 입니다.".format(answer))

# 출력 포멧 
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간확보 
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:왜<+10}".format(500))
print("{0:,}".format(10000000000))