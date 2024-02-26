# file : p25_usingModule.py
# desc : 모듈 사용

import calc # calc.py를 사용하겠다
from calc import mul # mul() 함수명만 쓰면 됨

from Math import Math # from Math는 모듈(파일이름) import Math는 클래스 이름

from day03.p22_carClass import Car

if __name__ == '__main__': ## java void main()과 동일
  result = mul(10,7)
  print(result)

  print(__name__) ## __main__ = 나는 메인엔트리야
