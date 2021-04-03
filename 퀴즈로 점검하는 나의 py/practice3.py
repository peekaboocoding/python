# 사이트 별로 비밀번호를 만들어주는 프로그램 작성하기 

# 예) http://naver.com
# 규칙 1: http:// 부분은 제외 => naver.com
# 규칙 2: 처음 만나는 점 (.) 이후 부분은 제외
# 규칙 3: 남은 글자중 처음 세자리(nav) + 글자갯수 + 글자내 'e' 갯수 + "!" 로 구성 

# 예) 생성된 비밀번호 nav51!

# 나의 예시 -- google
url ="http://google.com"
start_word = url.find('//') + 2
end_word = url.find('.')
# print(url[start_word:end_word])
word = url[start_word:end_word]

# 비밀번호 생성 규칙 
password = word[0:3] + str(len(word)) + str(word.count('e')) + '!'
print(password)



# 답안지 
my_word = url.replace('http://','')
my_word = my_word[:my_word.index('.')]

password = my_word[:3] + str(len(my_word)) + str(my_word.count('e')) + '!'

result = "{0} 의 비밀번호는 {1} 입니다.".format(url, password)
print(result)



