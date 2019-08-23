from PyQt5.QtCore import *

from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QTextEdit,QPushButton
from socket import socket 
from threading import Thread 
from PIL import Image

import sys 

class MainWindow(QMainWindow):
    def __init__(self,username = 'Nobody'):
        super().__init__()
        self.msg = []
        self.username = username

        """ Text Input """
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10,530,821,131)

        """ Chat Window """
        self.chat_window = QTextEdit(self)
        self.chat_window.setReadOnly(True)
        self.chat_window.setGeometry(10,10,941,511)

        """ Push Button Send """
        self.button_send = QPushButton(self)
        self.button_send.setText("Send")
        self.button_send.setGeometry(840,530,111,40)
        self.button_send.clicked.connect(self.Button_Send_Clicked)

        """ Push Button ImgTxt """
        self.button_imgtxt = QPushButton(self)
        self.button_imgtxt.setText("Image")
        self.button_imgtxt.setGeometry(840,576,111,40)
        self.button_imgtxt.clicked.connect(self.Button_ImgTxt_Clicked)

        """ Push Button Exit """
        self.button_exit = QPushButton(self)
        self.button_exit.setText("Exit")
        self.button_exit.setGeometry(840,622,111,40)
        self.button_exit.clicked.connect(self.Button_Exit_Clicked)
        
        """ Main Window """
        self.setGeometry(0,0,960,720)
        self.setWindowTitle("Image Filter GUI")
        self.show()

        """ Initialization """
        self.myclient = socket()
        self.myclient.connect(('10.186.7.28',9876))

    def Button_Exit_Clicked(self):
        content = "bye bye bye bye bye"
        self.myclient.send(content.encode('utf-8'))
        QApplication.quit()

    def Button_Send_Clicked(self):
        # self.msg = self.text_edit.toPlainText()
        # self.chat_window.append(self.username + ": " + self.msg)
        pass
        class RefreshScreenThread(Thread):
            def __init__(self,client,text_window,username):
                super().__init__()
                self._client = client
                self._text_window = text_window
                self._username = username
            def run(self): 
                while running:
                    data = self._client.recv(1024)
                    self._text_window.append(self._username + ": " + data.decode('utf-8'))
        running = True
        RefreshScreenThread(self.myclient,self.chat_window,self.username).start()
        while running:
            if self.text_edit.toPlainText() == '/exit' or self.text_edit.toPlainText() == '/logout':
                running = False
                content = "bye bye bye bye bye"
                self.myclient.send(content.encode('utf-8'))
                self.text_edit.clear()
            else:
                self.msg = self.text_edit.toPlainText()
                self.myclient.send(self.msg.encode('utf-8'))
                # self.chat_window.append(self.username + ": " + self.msg)
                self.text_edit.clear()

    def Button_ImgTxt_Clicked(self):
        try:
            self.file_path = QFileDialog.getOpenFileName(self,\
                "Open File","./",filter="PNG(*.png);;JPG(*.jpg)")
            if self.file_path[0]:
                self.file_name = (self.file_path[0].split('/'))[-1]

        except UnicodeDecodeError as why:
            self.error_box(why)
            pass

def main():
    username = input("Input your username: ")
    """
    RefreshScreenThread(myclient).start()
    while running:
        content = input()
        if content == 'bye bye':
            myclient.send(content.encode('utf-8'))
            running = False
        else:
            msg = username+': '+content 
            myclient.send(msg.encode('utf-8'))
    """
    
    """ Main Window Shown """
    app = QApplication(sys.argv)
    chat = MainWindow(username)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

