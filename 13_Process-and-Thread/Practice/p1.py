"""
Create a GUI with 2 buttons: Download and About
Make the thread Download individual so that even 
if the user has clicked on the button Download, 
s/he can still use the About button. 
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread 

def main():
    class Download(Thread):
        def run(self):
            t1 = time.time()
            time.sleep(10)
            t2 = time.time()
            tkinter.messagebox.showinfo('Info','Downloading Completed \
                \n %.2f sec' % (t2-t1))
            button1.config(state = tkinter.NORMAL)

    def download():
        button1.config(state = tkinter.DISABLED)
        Download(daemon = True).start()
    
    def About():
        tkinter.messagebox.showinfo('About','Love, D.Va')

    top = tkinter.Tk()
    top.title('Thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost',1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text = 'Download', command = download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text = 'About', command = About)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    main()