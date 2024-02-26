# file : p25_usingModule.py
# desc : 모듈 사용

import calc # calc.py를 사용하겠다
from calc import mul # mul() 함수명만 쓰면 됨

if __name__ == '__main__':
  result = mul(10,7)
  print(result)

  print(__name__) ## __main__ = 나는 메인엔트리야