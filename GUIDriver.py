"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from KB import KB
from UtilFuction import readPredicate, populate_FOL_KB, unify

global problemNo
problemNo = 0
global predicatefileName
predicatefileName = None
global ruleFileName
ruleFileName = None


class GUIDriver(QMainWindow):

    def __init__(self):
        super(GUIDriver, self).__init__()
        self.setGeometry(0, 30, 1450, 810)
        self.setWindowTitle("AI Assignment 4")
        self.nLabel = []
        self.nAnsLabel = []
        for i in range(30):
            self.nLabel.append(QtWidgets.QLabel(self))
            self.nAnsLabel.append(QtWidgets.QLabel(self))
        self.initGUI()

    def initGUI(self):

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Select Problem")
        self.label1.move(55, 0)

        self.lp1B = QtWidgets.QPushButton(self)
        self.lp1B.resize(150, 30)
        self.lp1B.move(20, 30)
        self.lp1B.setText("Logic Problem 1")
        self.lp1B.clicked.connect(self.logicP1)

        self.lp2B = QtWidgets.QPushButton(self)
        self.lp2B.resize(150, 30)
        self.lp2B.move(20, 60)
        self.lp2B.setText("Logic Problem 2")
        self.lp2B.clicked.connect(self.logicP2)

        self.lp3B = QtWidgets.QPushButton(self)
        self.lp3B.resize(150, 30)
        self.lp3B.move(20, 90)
        self.lp3B.setText("Logic Problem 3")
        self.lp3B.clicked.connect(self.logicP3)

        self.readPB = QtWidgets.QPushButton(self)
        self.readPB.resize(150, 30)
        self.readPB.move(210, 30)
        self.readPB.setText("Read Predicate")
        self.readPB.clicked.connect(self.readP)

        self.popuKbB = QtWidgets.QPushButton(self)
        self.popuKbB.resize(150, 30)
        self.popuKbB.move(210, 60)
        self.popuKbB.setText("Populate KB")
        self.popuKbB.clicked.connect(self.popuKb)

        self.unifyAlgoB = QtWidgets.QPushButton(self)
        self.unifyAlgoB.resize(150, 30)
        self.unifyAlgoB.move(210, 90)
        self.unifyAlgoB.setText("Unify algo")
        self.unifyAlgoB.clicked.connect(self.unify)

        self.readPB.setEnabled(False)
        self.popuKbB.setEnabled(False)
        self.unifyAlgoB.setEnabled(False)

        self.t1B.setEnabled(False)
        self.tb2.setEnabled(False)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Select Technique")
        self.label2.move(50, 140)
        self.label2.adjustSize()

        self.t1B = QtWidgets.QPushButton(self)
        self.t1B.resize(150, 30)
        self.t1B.move(20, 170)
        self.t1B.setText("Forward Chaining")
        self.t1B.clicked.connect(self.technique1)

        self.t2B = QtWidgets.QPushButton(self)
        self.t2B.resize(150, 30)
        self.t2B.move(20, 210)
        self.t2B.setText("Resolution")
        self.t2B.clicked.connect(self.technique2)

        self.resetB = QtWidgets.QPushButton(self)
        self.resetB.setText("RESET ALL")
        self.resetB.resize(150, 30)
        self.resetB.move(20, 250)
        self.resetB.clicked.connect(self.resetBclicked)

        # query label
        self.r1L = QtWidgets.QLabel(self)
        self.r1L.setText("")
        self.r1L.move(1000, 10)
        self.r1L.adjustSize()

        self.r2L = QtWidgets.QLabel(self)
        self.r2L.setText("")
        self.r2L.move(1000, 40)
        self.r2L.adjustSize()

        self.r3L = QtWidgets.QLabel(self)
        self.r3L.setText("")
        self.r3L.move(1000, 70)
        self.r3L.adjustSize()

        self.r4L = QtWidgets.QLabel(self)
        self.r4L.setText("")
        self.r4L.move(1000, 108)
        self.r4L.adjustSize()

        self.r5L = QtWidgets.QLabel(self)
        self.r5L.setText("")
        self.r5L.move(1000, 130)
        self.r5L.adjustSize()

        self.r6L = QtWidgets.QLabel(self)
        self.r6L.setText("")
        self.r6L.move(1000, 160)
        self.r6L.adjustSize()

        self.r7L = QtWidgets.QLabel(self)
        self.r7L.setText("")
        self.r7L.move(1000, 190)
        self.r7L.adjustSize()

        self.r8L = QtWidgets.QLabel(self)
        self.r8L.setText("")
        self.r8L.move(1000, 220)
        self.r8L.adjustSize()

        self.r9L = QtWidgets.QLabel(self)
        self.r9L.setText("")
        self.r9L.move(1000, 250)
        self.r9L.adjustSize()

        # 100node
        self.showtextbox = QTextEdit(self)
        self.showtextbox.move(5, 450)
        self.showtextbox.resize(700, 345)
        self.showtextbox.setLineWrapMode(QTextEdit.NoWrap)

        # instruction
        self.instrtL = QtWidgets.QLabel(self)
        self.instrtL.setText("**** INSTRUCTIONS ****\n\n"
                             "1.) readPredicate(), unify() and populate_fol_kb() is implemented.\n"
                             "2.) First click on any one of the logic problem, then select from type from right side (read predicate, populate kb, unify)\n"
                             "3.) Corresponding data will be shown in textbox below"
                             "4.) Click on ResetAll to reset and select different logic problem")
        self.instrtL.move(500, 20)
        self.instrtL.adjustSize()


    def paintEvent(self, event):
        line = QPainter()
        line.begin(self)
        line.setPen(Qt.red)

        line.drawLine(0,130,380,130)
        line.drawLine(180,0,180,280)
        line.drawLine(0,250,180,250)
        line.drawLine(0, 280, 180, 280)
        line.drawLine(380,0,380,130)


    def resetBclicked(self):
        global problemNo
        problemNo = 0
        global predicatefileName
        predicatefileName = None
        global ruleFileName
        ruleFileName = None
        self.lp1B.setEnabled(True)
        self.lp2B.setEnabled(True)
        self.lp3B.setEnabled(True)
        self.showtextbox.setText("")
        self.readPB.setEnabled(False)
        self.popuKbB.setEnabled(False)
        self.unifyAlgoB.setEnabled(False)

    def logicP1(self):
        global problemNo
        problemNo = 1
        global predicatefileName
        predicatefileName = "predicateFile1.txt"
        global ruleFileName
        ruleFileName = "ruleFile1.txt"
        self.lp1B.setEnabled(False)
        self.lp2B.setEnabled(False)
        self.lp3B.setEnabled(False)
        self.readPB.setEnabled(True)
        self.popuKbB.setEnabled(True)
        self.unifyAlgoB.setEnabled(True)

    def logicP2(self):
        global problemNo
        problemNo = 1
        global predicatefileName
        predicatefileName = "predicateFile2.txt"
        global ruleFileName
        ruleFileName = "ruleFile2.txt"
        problemNo = 2
        self.lp1B.setEnabled(False)
        self.lp2B.setEnabled(False)
        self.lp3B.setEnabled(False)
        self.readPB.setEnabled(True)
        self.popuKbB.setEnabled(True)
        self.unifyAlgoB.setEnabled(True)

    def logicP3(self):
        global problemNo
        problemNo = 1
        global predicatefileName
        predicatefileName = "predicateFile3.txt"
        global ruleFileName
        ruleFileName = "ruleFile3.txt"
        self.lp1B.setEnabled(False)
        self.lp2B.setEnabled(False)
        self.lp3B.setEnabled(False)
        self.readPB.setEnabled(True)
        self.popuKbB.setEnabled(True)
        self.unifyAlgoB.setEnabled(True)

    def technique1(self):
        pass

    def technique2(self):
        pass

    def readP(self):
        global problemNo
        global predicatefileName
        global ruleFileName
        self.showtextbox.setText("")

        readP = readPredicate(predicatefileName)
        self.showtextbox.append("Predicates after reading from file--\n")
        for i in readP:
            self.showtextbox.append(str(i))

    def popuKb(self):
        global problemNo
        global predicatefileName
        global ruleFileName
        self.showtextbox.setText("")
        self.showtextbox.append("Populating knowledge base from file--\n")
        kb = KB({}, [], {})
        kb = populate_FOL_KB(kb,ruleFileName)
        self.showtextbox.append("FACTS---")
        for x in kb.kbFactDict:
            self.showtextbox.append(str(x))
        self.showtextbox.append("\nRULES---(premise will be list of all predicates on right hand side connected with AND)")
        for x in kb.kbRule:
            self.showtextbox.append(str(x))


    def unify(self):
        self.showtextbox.setText("")

        self.showtextbox.append('Unifying fact = human(marcus) and query = human(X)')
        unifyResult = unify(['human', ['X']],['human',['marcus']],{})
        self.showtextbox.append("Substitution Result - " + str(unifyResult))

        self.showtextbox.append('Unifying fact = dead(marcus,79) and query = dead(marcus,Y)')
        unifyResult = unify(['dead', ['marcus', 'Y']],['dead',['marcus','79']],{})
        self.showtextbox.append("Substitution Result - " + str(unifyResult))

        self.showtextbox.append('Unifying fact = dead(marcus,79) and query = dead(X,Y)')
        unifyResult = unify(['dead', ['X', 'Y']],['dead',['marcus','79']],{})
        self.showtextbox.append("Substitution Result - " + str(unifyResult))

        self.showtextbox.append('Unifying fact = dead(marcus,79) and query = dead(jane,Y)')
        unifyResult = unify(['dead', ['jane', 'Y']], ['dead', ['marcus', '79']], {})
        self.showtextbox.append("Substitution Result - " + str(unifyResult))


def window():
    app = QApplication(sys.argv)
    window = GUIDriver()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
