# file : p65_flaskApp.py
# desc : 플라스크 웹서버

'''
> pip install flask
'''

from flask import Flask

app = Flask(__name__) # 현재의 모듈로 Flask 앱을 만들겠다.

@app.route('/')
def hello():
  return 'Hello, Flask!!'

@app.route('/1')
def testPage1():
    return 'Page1'

@app.route('/2')
def testPage1():
    return 'Page2'

def main():
  app.run(debug=True, port=80)

if __name__ == '__main__':
  main()
