# file: p66_imageEditor.py
# desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resource.qrc" -o "resources_rc.py"
를 통해 qrc파일을 파이썬에서 사용할 수 있도록 컴파일해줌
'''
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resources_rc

class winApp(QMainWindow):   # QWidget 아님
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day09/pyNewPaint.ui', self)
        self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowTitle('이미지에디터 v0.5')
        ## 이미지 추가
        pixmap = QPixmap('./day09/johnnaCute.jpg')
        self.lblCanvas.setPixmap(pixmap)

        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red

        ## UI 초기화 끝
        self.show()

    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널처리함수 선언...
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)

    def actionNewClicked(self):
        QMessageBox.about(self, '알림', '새그림')

    def actionOpenClicked(self):
        QMessageBox.about(self, '알림', '그림 열기')
    
    def actionSaveClicked(self):
        QMessageBox.about(self, '알림', '그림 저장')

    def actionExitClicked(self):
        QMessageBox.about(self, '알림', '프로그램 종료')

    def actionPenRedClicked(self):
        QMessageBox.about(self, '알림', '빨간펜')

    def actionPenGreenClicked(self):
        QMessageBox.about(self, '알림', '녹색펜')

    def actionPenBlueClicked(self):
        QMessageBox.about(self, '알림', '파란펜')

    def actionAboutClicked(self):
        QMessageBox.about(self, '알림', '프로그램 정보')

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end
        self.update() #화면 업데이트
    
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:QCloseEvent.accept()
        else:QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = winApp()
    sys.exit(app.exec_())