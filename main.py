import sys
from random import randint

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ellipse:
    def __init__(self, x, y, d, color):
        self.x, self.y, self.d, self.color = x, y, d // 2, color

    def draw(self, painter):
        painter.setPen(QPen(self.color, 3))
        # Там написано окружности, а не круги, но если имелись ввиду круги, то вот
        # painter.setBrush(QBrush(self.color))
        painter.drawEllipse(self.x - self.d, self.y - self.d, self.d * 2, self.d * 2)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(930, 815)
        self.verticalLayout_2 = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setMaximumSize(QSize(100, 25))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton.setText('Push me')
        self.setWindowTitle('Окружности')
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoRepeatInterval(0.2)
        self.pushButton.clicked.connect(self.add_ellipse)
        self.objects = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        for i in self.objects:
            i.draw(painter)
        painter.end()

    def add_ellipse(self):
        x = randint(0, self.size().width())
        y = randint(0, self.size().height())
        d = randint(10, 50)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.objects.append(Ellipse(x, y, d, color))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
