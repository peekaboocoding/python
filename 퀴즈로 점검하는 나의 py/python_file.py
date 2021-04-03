# 파일 내용 쓰기 
score_file = open("score.txt","w",encoding="utf8")
print("수학 : 100", file=score_file)
print("영어 : 90", file=score_file)
score_file.close()

# 파일 내용 추가하기 
score_file = open("score.txt","a",encoding="utf8")
score_file.write("과학 : 92\n")
score_file.write("국어 : 92")
score_file.close()

# 파일 내용 읽기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()