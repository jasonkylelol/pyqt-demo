from PyQt5.QtWidgets import QApplication
import sys

import qlineedit

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = qlineedit.lineEditDemo()
        win.show()
        sys.exit(app.exec_())