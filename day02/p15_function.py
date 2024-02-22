# file : p15_function.py
# desc : 함수 학습

def plus(a, b): # 매개변수 + 리턴값O
  res = a + b
  return res

def minus(a,b): # 매개변수, 리턴값x
  res = a - b
  print(res)

def multi(): # 매개변수x, 리턴값O
  global a, c # 밖에 있는 전역변수 a, c를 사용하겠다
  res = a * c
  return res

def divide():
  global a, c
  print(a / c)

# 기본인수
def pow(a,b=10): # 기본인수를 지정할때는 뒤에서부터
  res = a ** b
  return res

print('더하기')
a = 10
c = 7
result = plus(a,c)
print(result)

minus(a,c)
result = multi()
print(result)
divide()

print(pow(2, 3))
print(pow(2)) # 두번째 값을 안넣으면 b=10 디폴트 값으로 인식해서 계산 / 앞은 필수로 넣어야함

def plus_many(*items):
  result = 0
  for item in items:
    result += item
  return result

print(plus_many(1,2))
print(plus_many(1,2,3))
print(plus_many(1,2,3,4,5))


