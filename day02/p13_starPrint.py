# file : p13_starPrint.py
# desc : 별찍기

print('예제그림')
for i in range(1, 6):
  print('*' * i)

# 2중 for 문으로 만들기
print('\n')
print('별찍기 ------->')
for x in range(1,6):
  for y in range(x, 6):
    print('*', end='')
    #print(' ', end='')
    #print('*', end='')
  print()

