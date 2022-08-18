
import sys
#from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initSet(self):
        self.setWindowTitle('ppt Transform')
        self.move(300, 300)
        self.resize(800, 500)
        self.show()
              


    def initUI(self):
        #TextEdit
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.te.setText("가사를 입력하세요.")  # 지워지는 가사되야..
        #self.te.resize(300,20)  창 크기 따라 상대적으로 달라짐. 꽉 채워도 나쁘지 않아.
        



        #Label
        self.lbl = QLabel("생성")

        



        # layOut
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        


        self.initSet()
        # python 이 함수 호출 시, 자동으로 self 인자를 먼저 넘겨줌.


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())