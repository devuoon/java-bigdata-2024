# file : p39_naverNewsApp.py
# desc : PyQt5, QtDesigner,naver API 연동 뉴스검색 앱 만들기
'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from naverSearch import NaverSearch

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day06/naverNews.ui', self) # ui 파일 맞춰서 변경
        self.setWindowIcon(QIcon('./images/news.png')) # 아이콘 파일에 맞춰서 변경
        # 버튼 시그널처리 
        self.btnSearch.clicked.connect(self.btnSearchClicked) # ui파일내 위젯은 자동완성X 

        self.show()

    def btnSearchClicked(self): # 검색 버튼 클릭시 처리
        searchWord = self.txtSearchWord.text().strip()
        print(searchWord)
        
        if(len(searchWord.strip())) == 0: # Validation Check(입력 검증)
            QMessageBox.about(self, '네이버검색', '검색어를 입력하세요.')
            return # 함수 탈출

        # QMessageBox.about(self, '네이버검색', '검색시작')
        # 검색시작
        api = NaverSearch() # api 객체생성
        jsonSearch = api.getSearchResult(searchWord)
        print(jsonSearch)


    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept() # 진짜 닫음
        else:
            QCloseEvent.ignore() # 무시        

app = QApplication(sys.argv) 
inst = qtApp()
app.exec_()