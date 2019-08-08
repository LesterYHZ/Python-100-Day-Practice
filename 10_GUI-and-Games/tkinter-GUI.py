"""
Tk is the default package used to build Python GUI apps. Yet for 
better use, switch to PyQt5

Here are the steps of tkinter GUI building:
    1. Import the tkinter package and modules
    2. Create a top window object to hold all the GUI modules
    3. Add GUI parts onto the window object
    4. Connect the GUI parts to their relative functions
    5. Main loop
"""

import tkinter as tk
import tkinter.messagebox

def main():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg = ('red','Hello World!')\
            if flag else ('blue','See ya, World!')
        label.config(text=msg,fg=color)
    
    def confirm_to_quit():
        if tk.messagebox.askokcancel('Warning','You Sure to Quit?'):
            top.quit()
    
    # Create top window
    top = tk.Tk()
    # Set window geometry
    top.geometry('240x160')
    # Set window title
    top.title('Game')
    # Create label object and add it to the top window
    label = tk.Label(top,text='Hello, World!',font='Arial -32',fg='red')
    label.pack(expand=1)
    # Create a frame to hold button object
    panel = tk.Frame(top)
    # Create button objects and add them to the panel
    # Also, create callback functions
    button1 = tk.Button(panel,text='Edit',command = change_label_text)
    button1.pack(side='left')
    button2 = tk.Button(panel,text='Exit',command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # Main loop
    tk.mainloop()

if __name__ == '__main__':
    main()

