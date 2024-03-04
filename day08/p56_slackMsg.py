# file : p56_slackMsg.py
# dsec : 슬랙으로 스마트폰 메세지 보내기

import requests
import json

## 깃허브 업로드 전에 삭제
slack_url = ''

headers = {'Contents-type': 'application/json'}
data = {'text' : 'Python에서 보내는 메세지'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
  print('메세지 전송성공')
else:
  print('메세지 전송실패')