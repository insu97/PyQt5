import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt

class MyApp(QMainWindow) : # QWidget : 기본, QMainWindow : 메인창

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        
        # 폰트 설정
        QToolTip.setFont(QFont('SansSerif', 10))

        # 타이틀 제목, 아이콘
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('img/eng.png'))

        # 상태바 만들기
        ## self.statusBar().showMessage('Ready')

        ## 상태 표시줄에 날짜 표시하기
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # 윈도우 창 만들기
        ## self.move(300, 300)
        ## self.resize(400, 200)
        self.setGeometry(300, 300, 400, 200) # 위치 : (x , y) , 창 : (너비 , 높이)
        self.center()

        ## 종료 버튼 만들기
        btn = QPushButton('Quit', self) # 문구설정
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) # 적절한 크기로 변경
        btn.clicked.connect(QCoreApplication.instance().quit)

        ## 툴팁 버튼 만들기
        tooltip_btn = QPushButton('Button', self)
        tooltip_btn.setToolTip('This is a <b>QPushButton</b> widget')
        tooltip_btn.move(100, 100)
        tooltip_btn.resize(btn.sizeHint())
        
        # 메뉴바 만들기
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File') # Alt + F : 단축키
        filemenu.addAction(exitAction)

        self.show()

    def center(self):
        qr = self.frameGeometry() # 창의 위치와 크기 정보 가져오기
        cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp) # 가운데로 이동
        self.move(qr.topLeft())

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())