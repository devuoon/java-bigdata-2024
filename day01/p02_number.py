#file : p02_number.py
#desc : 숫자형 자료타입

age = 40 #int형 담는 변수
taxRate = 8.8 #float형을 담는 변수
highFloats = 4.24E10 #지수승(float)

print('나이는', age) #문자열이 "", '' 둘 다 사용가능
print('세율은', taxRate)
print('지수값', highFloats)


#틀수 숫자형
binVal = 0b11111111 #255 (컴터때문에)
octVal = 0o11 #9
hexVal = 0xFF #255
print('이진수', binVal, '팔진수', octVal, '16진수', hexVal)

#결론 : 타입을 적을 필요가 없다.
a, b, c = 3,4,5
print(a + b)
print(a - c)
print(a * c)
print(a / b)
#단, 나누기는 3가지로 분류
print(c / b)  #정확하게 실수로 나누기
print(c // b) #정수로만 나누기 몫
print(c % b) #정수로 나눈 나머지

print(2 ** 10) #2의10승
 
print((a + b) * c) #연산자 우선순위는 다 필요없고, ()괄호만 잘 쓰면 끝