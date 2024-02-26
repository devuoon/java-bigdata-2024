# file : p26_exceptionHandle.py
# desc : 예외처리
# 오류(Error) 코드상 빨간색(노란색) 밑줄이 그어지는 것
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 1. 파일 읽기 - 예외발생(2번으로 넘어가기 불가능)
f = open('./sample.txt', mode='r', encoding='utf-8')
#blah blah blah
res = f.readlin()
f.close()

# 2. 계산결과
#print(5 / 0)

#a, b = 5, 3
#if a < b:
#  print('True')
