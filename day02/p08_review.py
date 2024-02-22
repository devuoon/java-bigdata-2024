#file : p08_review.py
#desc : 리뷰

#Q2. 홀수, 짝수 판별하기
a = 13
print('a는', end='')
if a % 2 == 0:
    print('짝수')
else :
    print('홀수')
# 결과 : a는 홀수


#Q3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[0:6]
print(yyyymmdd) # 결과 : 881120
num = pin[7:]
print(num) # 결과 : 1068234


#Q5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(':', '#')  # ':'를 '#'로 대체
print(b) # 결과 : a#b#c#d


#06 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
print(a) # 결과 : [1,2,3,4,5]
a.reverse()
print(a) # 결과 : [5,4,3,2,1]


#Q10 딕셔너리 값 추출하기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # 결과 : ['A' : 90, 'C' : 70]
print(result) # 결과 : 80
