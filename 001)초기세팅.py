import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application & Icon & Quit Button')
        self.setWindowIcon(QIcon('img/eng.png'))

        # self.move(300, 300)
        # self.resize(400, 200)
        self.setGeometry(300, 300, 300, 200) # 위치 : (x , y) , 창 : (너비 , 높이)

        ## 버튼 만들기
        btn = QPushButton('Quit', self) # 문구설정
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())