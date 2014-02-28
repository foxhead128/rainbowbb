#! /usr/bin/env python3

import sys
from os.path import dirname, realpath
try:
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QApplication, QAction, QCheckBox, QComboBox, QPushButton, QDockWidget, QTextEdit, QMainWindow, QToolBar
except:
    try:
        from PyQt4.QtCore import Qt
        from PyQt4.QtGui import QApplication, QAction, QCheckBox, QComboBox, QPushButton, QDockWidget, QTextEdit, QMainWindow, QToolBar
    except:
        from PySide.QtCore import Qt
        from PySide.QtGui import QApplication, QAction, QCheckBox, QComboBox, QPushButton, QDockWidget, QTextEdit, QMainWindow, QToolBar

try: __file__
except: __file__ = sys.executable
app_lib = dirname(realpath(__file__))

sys.path.append(app_lib)

import rainbowbb

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)

def create_gradient(cycle):
    try: rainbowbb.cycles[cycle]
    except: return "transparent"
    else:
        picked_cycle = rainbowbb.cycles[cycle]
        increment = round(1/len(picked_cycle), 1)
        gradient = "qlineargradient(x1:0, y1:0, x2:0, y2:1"
        counter = increment
        for color in picked_cycle:
            gradient += ", stop:%s #%s" % (counter, color)
            counter += increment
        gradient += ")"
    return gradient

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle("RainbowBB")
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        self.toolBar = QToolBar(self)
        self.toolBar.setStyleSheet("QToolBar { background: %s; border: 0; border-top: 1px palette(shadow); border-bottom: 1px palette(shadow); }" % (create_gradient("pastel"),))
        self.toolBar.setMovable(False)
        self.toolBar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.addToolBar(self.toolBar)

        self.closeWindowAction = QAction(self)
        self.closeWindowAction.setShortcuts(["Ctrl+W", "Ctrl+Q"])
        self.closeWindowAction.triggered.connect(self.close)
        self.addAction(self.closeWindowAction)

        self.reverseBox = QCheckBox("&Reverse", self)
        self.toolBar.addWidget(self.reverseBox)

        self.byWordBox = QCheckBox("By &word", self)
        self.toolBar.addWidget(self.byWordBox)

        self.bounceBox = QCheckBox("&Bounce", self)
        self.toolBar.addWidget(self.bounceBox)
        
        self.sizeList = QComboBox(self)
        self.sizeList.addItem("None")
        for num in range(1, 8):
            self.sizeList.addItem(str(num))
        self.toolBar.addWidget(self.sizeList)
        
        self.cycleList = QComboBox(self)
        self.cycleList.addItem("pastel")
        for cycle in sorted(list(rainbowbb.cycles.keys())):
            if cycle != "pastel":
                self.cycleList.addItem(cycle)
        self.toolBar.addWidget(self.cycleList)
        
        self.convertButton = QPushButton("&Convert", self)
        self.convertButton.clicked.connect(self.convert)
        self.toolBar.addWidget(self.convertButton)

        self.inputDock = QDockWidget("Input", self)
        self.inputDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.inputDock.setContextMenuPolicy(Qt.CustomContextMenu)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.inputDock)

        self.inputField = QTextEdit(self)
        self.inputDock.setWidget(self.inputField)

        self.outputField = QTextEdit(self)
        self.outputField.setReadOnly(True)
        self.setCentralWidget(self.outputField)

    def show(self):
        self.setVisible(True)
        self.inputField.setFocus()

    def convert(self):
        self.outputField.setPlainText(rainbowbb.size(rainbowbb.colorize(self.inputField.toPlainText(), self.cycleList.currentText(), self.reverseBox.isChecked(), not self.byWordBox.isChecked(), self.bounceBox.isChecked()), self.sizeList.currentText() if self.sizeList.currentText() != "None" else None))

def main():
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
