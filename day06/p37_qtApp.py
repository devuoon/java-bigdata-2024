# file : p37_qtApp.py
# desc : PyQt5 앱 만들기(계속)

# PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
# Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크(멀티플랫폼)

# 설치 > pip install PyQt5

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPaintEvent, QPainter, QColor, QFont, QIcon
# QMainWindow, QLabel, QPushoButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력들을 다 사용할 수 있음)
from PyQt5.QtWidgets import *  # QApplication, QWidget, QMainWindow, QLabel

class qtApp(QWidget): # QWidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
  def __init__(self) -> None: 
    super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되어야 함
    self.initUI()

  def initUI(self):
    label = QLabel() # 라벨위젯(qt, PyQt), 라벨컨트롤(MFC, C#, Java Fx, Android)

    self.setGeometry((1920 - 300)//2, (1080-300)//2, 300, 200) # 바탕화면 정해진 위치에 넓이와 높이로 설정
    self.setWindowTitle('세번째 qt앱')
    self.setWindowIcon(QIcon('./images/windows.png'))
    # 화면 UI에서 추가 / 변경할 것
    btn1 = QPushButton('클릭', self)
    btn1.setGeometry(170,130,100,40)
    btn1.clicked.connect(self.btn1Clicked) # 버튼 클릭 시그널이 발생하면 이를 처리하는 함수 연결

    self.show() # 윈도우 창 실행(필수)

  def btn1Clicked(self):
    QMessageBox.about(self, '버튼클릭', '버튼을 눌렀습니다.')

  def closeEvent(self, QCloseEvent ) -> None: # 우리식으로 오버라이드(재정의)
    re = QMessageBox.question(self, '종료확인', '종료할까요?', QMessageBox.Yes|QMessageBox.No)
    if re == QMessageBox.Yes: #닫기
      QCloseEvent.accept()
    else:
      QCloseEvent.ignore() #닫지 않음

  def paintEvent(self, event) -> None:
    paint = QPainter() # 윈도우 창 위에 그림그리는 객체
    paint.begin(self) # 그림을 그리기 시작하면
    paint.setPen(QColor(200, 0, 0))
    paint.setFont(QFont('Bauhaus 93', 40))
    paint.end() # 반드시 닫아야 함

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실제 실행