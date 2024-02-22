# file : 07_variable.py
# desc : 변수에 대하여

z = 1
a = [1,2,3]
print(id(a))

b = a
print(id(b)) # b와 a의 id 값이 같다.

c = 1
d = c
print(id(c))
print(id(d)) # c와 d의 id 값이 같다.