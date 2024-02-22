# file : p10_forCondition.py
# desc : for 반복문

# for item in 반복할객체 :
#      ....(반복할 행동)

a = [1,2,3]
print(type(a)) # <class 'list'>
for i in a:
  print(type(i))

for i in ['one', 'two', 'three']:
  print(type(i))

b = [(1,2),(3,4),(5,6)] # tuple의 리스트

for i in b :
  print(type(i))

for(first, second) in b: # (first, second) 튜플의 괄호는 생략가능
  print(first, second)

# 평균내기
grade = [90, 80, 50, 70, 10]
sum = 0
for i in grade:
  sum += i

print(sum) #총합
print(sum / len(grade)) #평균

## range() **중요**
print(range(10))
print(range(0,10))

for i in range(0,10):
  print(i, end=', ')
print()

print(list(range(0, 10))) # 0부터 10미만까지
print(list(range(0,10,2))) # 0부터 10미만까지 2씩증가
print(list(range(1,10,2))) # 1부터 10미만까지 2씩증가

print(list(range(10,0,-2))) # 10부터 1이상까지 -2씩감소
print(list(range(4, 101, 4)))
print(list(range(10, 0, -1)))

res = 0
for i in range(1, 11):
  res += i

print(res)


# list comprehension \ 리스트 내포
# list(range()) 만으로도 리스트를 생성할 수 있지만, 여러조건으로 리스트를 생성할 때는 
print([i for i in range(1,11)])

print([num * 3 for num in range(1,1001) if num % 3 == 0])




