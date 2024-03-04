# file : p54_captWeather.py
# desc : 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

#auto.mouseInfo() # 80,154

regions = ['서울','강원','대전','대구','부산']
for region in regions:
  auto.moveTo(80,154, duration=0.5)
  auto.leftClick()
  for _ in range(5):
    auto.press('delete')
  time.sleep(0.2)

  clip.copy(f'{region} 날씨')
  auto.hotkey('ctrl','v')
  time.sleep(0.2)

  auto.press('\n')
  time.sleep(1.0)

  # 33, 278 / 696, 919
  startX, startY = 33, 278
  endX, endY = 696,919

  # auto.screentshot() 만 사용하면 acos에서 동작안함
  auto.screenshot(f'./day08/{region}날씨.png', region=(startX, startY, endX-startX, endY-startY))
  
print('저장완료')
