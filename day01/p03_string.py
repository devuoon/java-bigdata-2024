# file : p03_string.py
# desc : 문자열 자료형과 연산

a ="Hello World"
print(a)

b = 'Hello World'
print(b)

c = "Hello, 'Ashley'"
print(c)

#탈출문자 \n, \t외 나머지는 파이썬에서 잘 사용되지 않음

#문장을 여러줄 쓰고 싶으면
d = 'Hello~ \n'
'I\'m yoonji'
'Nice to meet you'

#여러줄 문장을 쓸때는 '''. """
d = '''Hello~
I'm yoonji.
Nice to meet you too'''
print(d)

# 문자열 연산 +, *
before = 'I wanna go to '
after = 'Boracai'

print(before + after) #I wanna go to Boracai (문자열을 합쳐서 하나의 문자열)
print(after * 3) #BoracaiBoracaiBoracai (문자열을 몇 번 반복)
