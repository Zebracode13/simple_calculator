import sys

from PyQt5.QtWidgets import(QGridLayout, QLineEdit, QMainWindow,
         QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette 

class PyCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator-Zele")
        # self.setFixedSize(175, 250)

        self.palette = QPalette()
        self.myLayout = QVBoxLayout()
        self.myWidget = QWidget(self)



        self.palette.setColor(QPalette.Button, Qt.yellow)
        self.palette.setColor(QPalette.Text, Qt.blue)
        self.palette.setColor(QPalette.Background, Qt.black)

        self.setPalette(self.palette)
        self.myWidget.setPalette(self.palette)

        self.setCentralWidget(self.myWidget)
        self.myWidget.setLayout(self.myLayout)

        self.createDisplay()
        self.CreateButtons()
       

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        # self.display.setReadOnly(True)

        self.display_font = QFont()
        self.display_font.setPixelSize(30)

        self.display.setFont(self.display_font)
        self.display.setAlignment(Qt.AlignRight)
        self.myLayout.addWidget(self.display)

    def CreateButtons(self):
        self.buttons = {}
        self.buttonLayout = QGridLayout()

        button = {
            'C': (0,0),
            '+|-':(0,1),
            '%': (0,2),
            '/': (0,3),
            # 
             '7': (1,0),
            '8': (1,1),
            '9': (1,2),
            '*': (1,3),
            # 
             '4': (2,0),
            '5': (2,1),
            '6': (2,2),
            '-': (2,3),
            # 
             '3': (3,0),
            '2': (3,1),
            '1': (3,2),
            '+': (3,3),
            # 
             '0': (4,0),
            '.': (4,1),
            '00': (4,2),
            '=': (4,3),
        }

        for butt, loc, in button.items():
            self.buttons[butt] = QPushButton(butt)
            self.buttons[butt].setFixedSize(40,40)
            self.buttonLayout.addWidget(self.buttons[butt], loc[0], loc[1])
            
        self.myLayout.addLayout(self.buttonLayout)

    def setDisplayText(self, txt):
        self.display.setText(txt)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.display.setText("")








    





