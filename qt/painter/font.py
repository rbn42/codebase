

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we draw text in Russian azbuka.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 780, 770)
        self.setWindowTitle('Draw text')
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        text = """
        一二三一二三一二三一二三一二三一二三一二三一二三一二三一二三一二三一二三
        112233112233112233112233112233112233112233112233112233112233112233112233
        aabbccaabbccaabbccaabbccaabbccaabbccaabbccaabbccaabbccaabbccaabbccaabbcc
        1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 
        a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c 
        """
        qp.setPen(QColor(168, 34, 3))
        family = "WenQuanYi Micro Hei Mono"
        family = "monospace"
        family = "monaco,WenQuanYi Micro Hei Mono"
        f = QFont(family, 20)
        f.setUnderline(True)
        qp.setFont(f)
        qp.drawText(event.rect(), Qt.AlignCenter, text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
