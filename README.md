# 빅데이터 언어 2024

빅데이터 자바 개발자 파이썬 학습 리포지토리

## 1일차

- 파이썬 개발환경

  - 깃헙 가입
  - 깃 설치
  - 깃헙 데스크탑 설치
  - 파이썬 설치
  - Visual Studio Code 설치
  - 나눔고딕코딩 글자체 설치

- 파이썬 학습

  - 파이썬 개요
  - 파이썬 기초문법

    - 숫자형(정수, 실수, 진수)

    ```python
    #틀수 숫자형
    binVal = 0b11111111 #255 (2진수)
    octVal = 0o11 #9 (8진수)
    hexVal = 0xFF #255 (16진수)
    print('이진수', binVal, '팔진수', octVal, '16진수', hexVal)
    ```

    - 문자열형(연산, 문자열 포맷, 함수)
    - 리스트형, 튜플형(연산, 함수)

## 2일차

- 파이썬 학습
  - 파이썬 기초문법
    - 딕셔너리, 집합
    - 불형
    - None형
    - 제어문 (if, for, while)
    - 제어문 연습
    - 함수

## 3일차

- 파이썬 학습
  - 파이썬 기초문법
    - 입출력
    - 객체지향
    - 모듈
    - 패키지

## 4일차

- 파이썬 학습
  - 파이썬 기초문법
    - 모듈, 패키지
    - ★★ 예외처리, 디버깅 : 디버깅하면서 예외처리
    - 내장함수
    - 표준 및 외부 라이브러리

## 5일차

- 파이썬 학습

  - 파이썬 응용

    - 아스키 및 유니코드
    - 주소록 앱 만들기

    ```python
      class Contact: # 주소록 클래스
      # 생성자
      __name = ''
      __phoneNumber = ''
      __eMail = ''
      __addr = ''

      def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

      # 사용자가 원하는 형태로 출력
      def __str__(self) -> str:
        res = (f'이  름 : {self.__name}\n'
                f'핸드폰 : {self.__phoneNumber}\n'
                f'이메일 : {self.__eMail}\n'
                f'주  소 : {self.__addr}\n')
        return res

      # 연락처 여부 확인
      def isNameExist(self, name):
        if self.__name == name: # 찾는 이름 존재
          return True
        else:
          return False

      def getInfo(self):
        return self.__name, self.__phoneNumber, self.__eMail, self.__addr
    ```

    ![주소록앱](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata01.gif)

    - Windows Application(PyQt)

    ![QtApp](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata02.png)

## 6일차

- 파이썬 학습
  -PyQt5 학습 이어서

  - QWidget 자식 클래스 종류 학습

  ![QLbel](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata03.png)

  - Naver 뉴스API 검색 앱

  ![naverApp](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata04.png)

## 7일차

- 파이썬 학습

  - PyQt5 계속
    - Naver 뉴스 API 검색 앱 마무리
  - json 학습
  - PyQt5

    - 스레드 개념, 학습

    ![스레드](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata05.png)

    - TTS
    - QRCode 생성기

    ![QR](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata06.png)

    - 구글번역기앱

    ![구글번역](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata07.png)

## 8일차

- 파이썬 응용

  - 파이썬 자동화

    - PyAutoGui 모듈(마우스, 키보드, 화면캡처)
    - 슬랙 webhook로 모바일 메시지 전송

    <!-- ![슬랙](https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata08.jpg) -->
    <img src="https://raw.githubusercontent.com/devuoon/java-bigdata-2024/main/images/bigdata08.jpg" width="250">

    - Tesseract 프로그램으로 이미지에서 글자 추출
