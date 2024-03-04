# file : p55_katalkAuto.py
# desc : 카톡 PC에서 자동으로 메세지 보내기
# 

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateAllOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.click(clickPos)
time.sleep(0.5)

groupLoc = auto.locateAllOnScreen('./day08/findLoc2.png')
clickPos = auto.center(groupLoc)
auto.doubleClick(clickPos)
time.sleep(0.2)

clip.copy('자동으로 보내는 메세지')
auto.hotkey('ctrl','v')
auto.press('\n')