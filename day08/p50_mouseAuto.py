# file : p50_mouseAuto.py
# desc : pyAutoGui로 마우스 조작

'''
PyAutoGui 모듈 설치시 명령 프롬포트보다 VSCode내 터미널에서 설치를 추천
>> pip install pyautogui
'''

import pyautogui as auto

print(auto.size()) # 모니터 해상도 정보
print(auto.position()) # 현재 마우스의 위치

#pyautogui 마우스설정 창
#pullow 모듈이 같이 설치되어야 색상 표시가능
#auto.mouseInfo()

## 마우스 이동 (절대좌표)
auto.moveTo(622,53) # (0, 0) 이후 이동이 안됨
auto.moveTo(622, 53, duration=0.1) # x축 622 y축 53으로 1.0초동안 이동
auto.moveTo(1210, 568, duration=0.1) 

## 마우스 이동 (상대좌표)
#auto.move(500,500, duration=0.5) # 현재위치에서 x축 500, y축 500으로 1.5초동안 이동

## 마우스 클릭
# auto.leftClick(x=622, y=53) # 해당위치로 가서 바로 왼쪽버튼 클릭
# auto.rightClick(x=700, y=300) 
auto.click(clicks=4, interval=0.1, button='left') # 왼쪽버튼을 소스코드 에디어테엇 네번 선택하면 모든 글을 전체선택

## 마우스 드래그
auto.leftClick(x=1422, y=168, duration=1.0) # 1422, 168 에서 왼쪽 마우스 클릭 후 1초 대기
auto.dragTo(x=983, y=550, duration=2.0, button='left')
#auto.dragRel(500, 400, duration=1.0, button='left') # 현재위치에서 500, 400으로 1초 동안 드래그

## 마우스 휠
auto.scroll(1000) # 양수는 위로
auto.scroll(-300) # 음수는 아래로



