# file : p66_imageEditor.py
# desc : PyQt 이미지 에디터

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WinApp(QMainWindow): # QWidget이 아님
  def __init__(self) -> None:
    super().__init__()
    self.initUI()

  def initUI(self):
    uic.loadUi('./day09/pyNewPaint.ui', self)
    self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ins = WinApp()
  sys.exit(app.exec_())