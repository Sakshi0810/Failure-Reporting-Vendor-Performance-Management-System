import tkinter as tk
from tkinter import messagebox

class Window:

    def __init__(self, root):
        self.root = root

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.username.set('admin')
        self.password.set('password')


        self.btnlogin = tk.Button(root, text='login', command=self.Login_System)
        self.btnreset = tk.Button(root, text='change password', command=self.Reset)

        self.lbluser = tk.Label(root, text='username', textvariable='Username')
        self.lblpassword = tk.Label(root, text='password', textvariable='Password')

        self.entryuser = tk.Entry(root)
        self.entrypassword = tk.Entry(root)
        self.btnlogin.pack()
        self.btnreset.pack()
        self.lbluser.pack()
        self.entryuser.pack()
        self.lblpassword.pack()
        self.entrypassword.pack()

    def Login_System(self):
        u = self.entryuser.get()
        p = self.entrypassword.get()
        if u == self.username.get() and p == self.password.get():
            tk.messagebox.showinfo('Login successful','Welcome')
        else:
            tk.messagebox.showinfo('Login unsuccessful','Try again')

            self.entryuser.focus()

    def Reset(self):
        self.username.set(self.entryuser.get())
        self.password.set(self.entrypassword.get())
        self.entryuser.focus()



root = tk.Tk()
application = Window(root)
root.mainloop()
