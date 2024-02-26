# file : p30_standartLib.py
# desc : 표준 라이브러리(빌트인) 학습

import datetime

print(datetime.date(2024, 2, 26)) # 현재의 OS에 맞춰서 날짜형으로 변경

## 정말 많이 씀
curr = datetime.datetime.now() # 현재의 년월일시분초를 알려줌
print(curr)

print(curr.weekday()) #월요일 = 0 , 화요일 = 1 .... 일요일 = 6

print(curr.weekday())
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.hour)
print(curr.minute)
print(curr.second)

print(f'{curr.year}년 {curr.month}월 {curr.day}일 {curr.hour}시 {curr.minute}분 {curr.second}초')

