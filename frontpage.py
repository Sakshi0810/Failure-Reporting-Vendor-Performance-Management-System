import tkinter as tk
from PIL import ImageTk,Image
from tkinter import*
import random
import time
window = tk.Tk()
window.geometry("4000x4000")
background_image=ImageTk.PhotoImage(file="C:/Users/KIIT/Desktop/SAKSHI/rdso project/train1.jpg")
background_label = tk.Label(image=background_image,width=20,height=10)
background_label.image = background_image
label0 =tk.Label(window,font = ('Arial', 30,'italic'),fg="white",height=210,image=background_image,bg="white")
label0.grid(row = 1, column =1)
label1 =tk.Label(window,text="Failure Reporting And Vendor Performance\nManagement Application\n",padx=20,pady=20,font = ('Times New Roman', 36,'italic'),bg="white",fg="black",width=40,height=3,relief=SUNKEN,borderwidth=0)
label1.grid(row = 1, column =2)
window.title("Failure Reporting And Vendor Performance Management Application")
window.config(bg="white")

loginbutton = tk.Button(window,text="Login",padx=10,pady=10,borderwidth=2,font=('Times New Roman',16),height=2,width=10,bg="steelblue1").place(x=15,y=220)

dashboard = tk.Button(window,text= "Dashboard",padx=10,pady=10,borderwidth=2,font=('Times New Roman',16),height=2,width=10,bg="steelblue1").place(x=180,y=220)

homebutton = tk.Button(window,text="Home",padx=10,pady=10,borderwidth=2,font=('Times New Roman',16),height=2,width=10,bg="steelblue1").place(x=345,y=220)

changepassword = tk.Button(window,text= "Change password",padx=10,pady=10,borderwidth=2,font=('Times New Roman',16),height=2,width=10,bg="steelblue1").place(x=510,y=220)

newsec = tk.Button(window,text="Add new section",padx=10,pady=10,borderwidth=2,height=2,font=('Times New Roman',16),width=10,bg="steelblue1").place(x=675,y=220)

newitem = tk.Button(window,text= "Add new item",padx=10,pady=10,borderwidth=2,height=2,font=('Times New Roman',16),width=10,bg="steelblue1").place(x=840,y=220)

update_or_delete_item = tk.Button(window,text="Update or delete item",padx=10,pady=10,borderwidth=2,height=2,font=('Times New Roman',16),width=14,bg="steelblue1").place(x=1005,y=220)

add_failure_feature = tk.Button(window,text= "Add failure feature",padx=10,pady=10,borderwidth=2,height=2,font=('Times New Roman',16),width=12,bg="steelblue1").place(x=15,y=320)

delete_failure_feature = tk.Button(window,text= "Delete failure feature",padx=10,pady=10,borderwidth=2,height=2,font=('Times New Roman',16),width=14,bg="steelblue1").place(x=210,y=320)

item_warrenty= tk.Button(window,text= "Item warrenty",padx=10,pady=10,height=2,font=('Times New Roman',16),width=10,borderwidth=2,bg="steelblue1").place(x=430,y=320)

addnewvendor_or_updatenewvendor = tk.Button(window,text= "Add or update new vendor",padx=10,pady=10,height=2,font=('Times New Roman',16),width=18,bg="steelblue1").place(x=600,y=320)

itemvendor= tk.Button(window,text= "Item-vendor",padx=10,pady=10,height=2,font=('Times New Roman',16),width=10,borderwidth=2,bg="steelblue1").place(x=865,y=320)

allzonereport= tk.Button(window,text= "All zone report",padx=10,pady=10,height=2,font=('Times New Roman',16),width=10,borderwidth=2,bg="steelblue1").place(x=1040,y=320)

printviewreport = tk.Button(window,text= "Print or view report",padx=10,pady=10,height=2,font=('Times New Roman',16),width=14,borderwidth=2,bg="steelblue1").place(x=15,y=420)

supervisorreport= tk.Button(window,text= "Supervisor Report",padx=10,pady=10,height=2,font=('Times New Roman',16),width=14,borderwidth=2,bg="steelblue1").place(x=230,y=420)

window.mainloop()
