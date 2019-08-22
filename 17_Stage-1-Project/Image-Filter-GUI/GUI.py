from PyQt5.QtCore import *

from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QGraphicsScene
from PyQt5.QtWidgets import QComboBox,QPushButton,QLabel,QMessageBox, QSizePolicy
from PyQt5.QtGui import QIcon,QPixmap
from PIL import Image,ImageFilter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt
import pyqtgraph as pg 

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.img = None
        self.im = None
        self.file_path = None 

        """ Filter Combo Box """
        self.combo_Filter = QComboBox(self)
        self.combo_Filter.addItems(['<Select Filter>',\
                            'BLUR',\
                            'CONTOUR', \
                            'DETAIL', \
                            'EDGE_ENHANCE',\
                            'EDGE_ENHANCE_MORE',\
                            'EMBOSS',\
                            'FIND_EDGES',\
                            'SHARPEN',\
                            'SMOOTH',\
                            'SMOOTH_MORE'])
        self.combo_Filter.setGeometry(50,200,450,40)

        self.combo_Filter.currentIndexChanged.connect(self.combo_Filter_callback)

        """ Push Button Open """
        self.pushbutton_open = QPushButton(self)
        self.pushbutton_open.setGeometry(50,30,200,50)
        self.pushbutton_open.setText("Open")

        self.pushbutton_open.clicked.connect(self.Pushbutton_Open_callback)

        """ Push Button Confirm and Save """
        self.pushbutton_ConfirmandSave = QPushButton(self)
        self.pushbutton_ConfirmandSave.setGeometry(50,800,450,120)
        self.pushbutton_ConfirmandSave.setText("Confirm and Save")

        self.pushbutton_ConfirmandSave.clicked.connect(self.Pushbutton_ConfirmandSave_callback)

        """ Push Button Exit """
        self.pushbutton_exit = QPushButton(self)
        self.pushbutton_exit.setGeometry(300,30,200,50)
        self.pushbutton_exit.setText("Exit")

        self.pushbutton_exit.clicked.connect(self.Pushbutton_Exit_callback)

        # self.imv = pg.ImageView(self)
        # self.imv.setGeometry(300,30,500,500)
        # self.imv.show()

        """ Main Window """
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Image Filter GUI")
        self.show()

    """ Push Button Confirm and Save Callback Function """
    def Pushbutton_ConfirmandSave_callback(self):
        try:
            save_dialog = QFileDialog()
            save_dialog.setAcceptMode(QFileDialog.AcceptSave)
            save_path = save_dialog.getSaveFileName(self, 'Save as...', './',
                                                    filter='PNG(*.png)')
            if save_path[0]:
                self.im.save(save_path[0], "PNG")
                QMessageBox.about(self, "Saved", "Image Saved")
                plt.close()
        except FileNotFoundError as why:
            self.error_box(why)
            pass 

    """ ComboBox Callback Function """
    def combo_Filter_callback(self,idx):
        self.im = self.img
        if idx == 1:
            self.im = self.img.filter(ImageFilter.BLUR)
        elif idx == 2:
            self.im = self.img.filter(ImageFilter.CONTOUR)
        elif idx == 3:
            self.im = self.img.filter(ImageFilter.DETAIL)
        elif idx == 4:
            self.im = self.img.filter(ImageFilter.EDGE_ENHANCE)
        elif idx == 5:
            self.im = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif idx == 6:
            self.im = self.img.filter(ImageFilter.EMBOSS)
        elif idx == 7:
            self.im = self.img.filter(ImageFilter.FIND_EDGES)
        elif idx == 8:
            self.im = self.img.filter(ImageFilter.SHARPEN)
        elif idx == 9:
            self.im = self.img.filter(ImageFilter.SMOOTH)
        elif idx == 10:
            self.im = self.img.filter(ImageFilter.SMOOTH_MORE)
        m = PlotCanvas(self, width=13, height=9,img = self.im)
        m.move(600,30)

    """ Pushbutton Open Callback Function """
    def Pushbutton_Open_callback(self):
        try:
            self.file_path = QFileDialog.getOpenFileName(self,\
                "Open File","./",filter="PNG(*.png);;JPG(*.jpg)")
            if self.file_path[0]:
                self.combo_Filter.setEnabled(True)
                self.pushbutton_ConfirmandSave.setEnabled(True)
                self.file_name = (self.file_path[0].split('/'))[-1]
                self.img = Image.open(self.file_path[0])
                m = PlotCanvas(self, width=13, height=9,img = self.img)
                m.move(600,30)
        except UnicodeDecodeError as why:
            self.error_box(why)
            pass

    """ Pushbutton Exit Callback Function """
    def Pushbutton_Exit_callback(self):
        plt.close()
        QApplication.quit()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100,img=None):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(img)


    def plot(self,img):
        ax = self.figure.add_subplot(111)
        ax.imshow(img)
        self.show()

def main():
    app = QApplication(sys.argv)
    ifgui = MainWindow()
    ifgui.combo_Filter.setEnabled(False)
    ifgui.pushbutton_ConfirmandSave.setEnabled(False)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

