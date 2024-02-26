# file : p31_externalLib.py
# desc : 외부라이브러리 사용법

# > pip install LibName
# Successfully installed / Requrement already satisfied가 나와야 함
# > pip uninstall LibName
# Successfully uninstalled 나와야 함

from faker import Faker

dummy = Faker('ko-KR') #한국어
print(dummy.items().pop())
