from Calculator_UI import Ui_MainWindow

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator


READY = 0
INPUT = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        for n in range(0,10):
            getattr(self,"pushButton_n%s" % n).pressed.connect(lambda v=n: self.input_number(v))
        
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))
        self.pushButton_div100.pressed.connect(self.div100)
        self.pushButton_equ.pressed.connect(self.equ)

        self.pushButton_RE.pressed.connect(self.reset)
        self.pushButton_M.pressed.connect(self.store)
        self.pushButton_MR.pressed.connect(self.recall)

        self.memory = 0

        self.reset()

        self.show()

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None 
        self.display()

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v 
        else:
            self.stack[-1] = self.stack[-1]*10+v
        self.display()

    def display(self):
        self.lcdNumber.display(self.stack[-1])

    def operation(self,op):
        if self.current_op:
            self.equ()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op 

    def div100(self):
        self.state = INPUT 
        self.stack[-1] *= 0.01
        self.display()

    def equ(self):
        if self.state == READY and self.last_operation:
            s,self.current_op = self.last_operation 
            self.stack.append(s)
        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op
            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()

    def store(self):
        self.memory = self.lcdNumber.value()

    def recall(self):
        self.state = INPUT 
        self.stack[-1] = self.memory 
        self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculator")
    window = MainWindow()
    app.exec_()
