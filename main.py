from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys

import qlineedit, qpushbutton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win = qlineedit.lineEditDemo()
    # win = qpushbutton.PushButton()
    win = qpushbutton.ToolButton()
    win.show()
    win.setWindowIcon(QIcon('favicon.png'))
    sys.exit(app.exec_())