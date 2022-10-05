import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('My First Application') # 창의 제목

        self.move(300, 300) # 이 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(400,200) # 위젯의 크기를 너비 400px, 높이 200px로 조절

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())