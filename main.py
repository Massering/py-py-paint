import sys
from PyQt5 import uic
from random import randint

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ellipse:
    def __init__(self, x, y, d):
        self.x, self.y, self.d = x, y, d // 2

    def draw(self, painter):
        painter.drawEllipse(self.x - self.d, self.y - self.d, self.d * 2, self.d * 2)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.pressed.connect(self.add_ellipse)
        self.pushButton.setAutoRepeatInterval(3)
        self.pushButton.setAutoRepeat(True)
        self.objects = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(QColor(255, 235, 30), 4))

        for i in self.objects:
            i.draw(painter)

        painter.end()

    def add_ellipse(self):
        x = randint(0, self.size().width())
        y = randint(0, self.size().height())
        d = randint(10, 50)
        self.objects.append(Ellipse(x, y, d))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
