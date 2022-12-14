import sys
from random import randint

from PyQt5 import uic, QtGui
from UI import Ui_Form
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.repaint()

    def paintEvent(self, event):
        if self.sender():
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        radius = randint(10, 200)
        x, y = randint(10, 200), randint(10, 200)
        qp.drawEllipse(x, y, radius, radius)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())