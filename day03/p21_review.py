# Q7. 파일의 문자열 바꾸기
f = open('test.txt', 'r')
# test.txt의 내용을 body 변수에 저장
body = f.read()
f.close()

# body 문자열에서 'java'를 'python'으로 바꾸기
body = body.replace('java', 'python')

# 파일을 쓰기 모드로 다시 실행
f = open('test.txt', 'w')
f.write(body)
f.close()
