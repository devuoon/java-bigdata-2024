# file : p09_ifCondition.py
# desc : if 제어문

money = 1000
if money >= 5000 :
  # indentation(들여쓰기) tab == space 2번
  print('택시타고 가')
  print('부럽네')
elif money < 5000 and money >= 2500:
  print('기사님 홈플러스앞까지만 가주세요')
  print('집까지 걸어감')
else:
  print('걸어가~')
  print('돈도 없는게...')

a, b, c, d = 10, 5, 7, 9

print(a >= b) #True
print(c > d)  #False

print(a >= b and c > d) #False
print(a >= b or c > d) #True

print(not (a >= b)) #False

## print() end옵션(많이 사용), sep옵션
print(1 in [1,3,5,7,9], end =',') #True
print(6 in [1,3,5,7,9]) #False

print('13579', '246810', sep = '|')

score = 60

print('success' if score >= 60 else 'falure')
