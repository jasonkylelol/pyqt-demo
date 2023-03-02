from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QDialog, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>PythonPyQt.com</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>QLabel2</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('Hint')
        label3.setPixmap(QPixmap("imgs/python.png"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://python.org'>Python.org</a>")
        label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip('Python.org')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel Example')

    def linkHovered(self):
        print('Link hovered')

    def linkClicked(self):
        print('Link clicked')

class QLabelBuddy(QDialog) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel Example')
        self.setFixedWidth(250)

        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)