from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys

import qlineedit, qpushbutton, qtextedit, qlabel, qmessagebox

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win = qlineedit.lineEditDemo()
    # win = qpushbutton.PushButton()
    # win = qpushbutton.ToolButton()
    # win = qtextedit.TextEditDemo()
    # win = qlabel.QLabelDemo()
    # win = qlabel.QLabelBuddy()
    win = qmessagebox.Example()
    win.show()
    win.setWindowIcon(QIcon('imgs/favicon.png'))
    sys.exit(app.exec_())