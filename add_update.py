from tkinter import*
import tkinter.messagebox
import venddatabase

class Vendor(tkinter.Frame):
    def __init__(self,root1):
        self.root1 = root1
        super(Vendor, self).__init__()
        self.root1.title("vendor management")
        self.root1.geometry("1350x7500+0+0")
        self.root1.config(bg="white")
        vendor_name = StringVar()
        vendor_id = StringVar()
        #===============================================Frames=================================
        def iEXIT():
            iEXIT=tkinter.messagebox.askyesno("vendor management","confirm if you want to exit")
            if iEXIT>0:
                root1.destroy()
                return


        def addData():
            if(len(vendor_id.get())!=0):
                venddatabase.addvendor(vendor_id.get(),vendor_name.get())
                vendorlist.delete(0,END)
                vendorlist.insert(END,(vendor_id.get(),vendor_name.get()))
        def DisplayData():
            vendorlist.delete(0,END)
            for row in venddatabase.viewData():
                vendorlist.insert(END,row,str(""))
        def vendRec(event):
            global vd
            searchVend= vendorlist.curselection()[0]
            vd=vendorlist.get(searchVend)
            self.integervendor_id.delete(0,END)
            self.integervendor_id.insert(END,vd[1])
            self.txtvendor_name.delete(0,END)
            self.txtvendor_name.insert(END,vd[1])
        def Update():
            if(len(vendor_id.get())!= 0):
                venddatabase.addvendor(vendor_id.get(),vendor_name.get())
                venddatabase.insert(END,(vendor_id.get(),vendor_name.get()))
        MainFrame = Frame(self.root1,bg="white")
        MainFrame.grid()
        titleFrame = Frame(MainFrame,bd=2,padx=20,pady=8, bg="Ghost white",relief=RIDGE)
        titleFrame.pack(side=TOP)
        self.lbltitle=Label(titleFrame,font=('arial',30,'bold'),text="VENDOR MANAGEMEMT",bg="Ghost White")
        self.lbltitle.grid()
        buttonf=Frame(MainFrame,bd=2,width=90,height=50,padx=18,pady=20,bg="Ghost White",relief=RIDGE).place(x=8,y=600)

        dataf = Frame(MainFrame, bd=1, width=1900, height=300, padx=20, pady=20, bg="Cadet blue", relief=RIDGE)
        dataf.pack(side=BOTTOM)
        datafl = LabelFrame(MainFrame, bd=1, width=500, height=360, padx=2,pady=3,font=('arial',20,'bold'),text="vendor info",bg="Ghost White", relief=RIDGE)
        datafl.pack(side=LEFT)
        datafr = LabelFrame(MainFrame, bd=1, width=450, height=330, padx=7,pady=3,bg="Ghost White", relief=RIDGE,font=('arial',20,'bold'),text="vendor details").place(x=1000,y=100)


        self.lblvend = Label(datafl, font=('arial', 15, 'bold'), text="vendor id", bg="Ghost White").place(x=0,y=50)
        self.lblvend = Entry(datafl, font=('arial', 20, 'bold'), textvariable= vendor_id,width=20).place(x=130,y=50)
        self.lblvends = Label(datafr, font=('arial', 15, 'bold'), text="vendor name", bg="Ghost White").place(x=0, y=200)
        self.lblvends = Entry(datafr, font=('arial', 20, 'bold'), textvariable=vendor_name, width=20).place(x=130, y=200)

        scrollbar=Scrollbar(datafr)
        scrollbar.grid(row=0,column=1,sticky='ns')
        vendorlist=Listbox(datafr,width=41,height=16,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)

        scrollbar.config(command=vendorlist.yview)

        self.btnaddvendor=Button(buttonf,text="Add new",font=('arial',12,'bold'),height=3,width=10,bd=2,command=addData,bg="Ghost White").place(x=8,y=600)

        self.upvendor = Button(buttonf, text="update", font=('arial', 12, 'bold'), height=3, width=10, bd=2,command=Update,bg="Ghost White").place(x=200,y=600)
        self.disvendor = Button(buttonf, text="display", font=('arial', 12, 'bold'), height=3, width=10, bd=2,command=DisplayData,bg="Ghost White").place(x=450, y=600)
        self.exvendor = Button(buttonf, text="exit", font=('arial', 12, 'bold'), height=3, width=10, bd=2,command=iEXIT,bg="Ghost White").place(x=650, y=600)


if __name__ == '__main__':
    root= tkinter.Tk()
    application = Vendor(root)
    root.mainloop()
