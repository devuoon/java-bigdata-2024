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
