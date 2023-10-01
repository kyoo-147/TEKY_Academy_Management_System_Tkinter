# -*- coding: utf-8 -*-
# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

from os import path
from tkinter import *
from tkinter import ttk, messagebox
import json

class Disp():
    def __init__(self,window,wid,hg):
        self.rt = window
        self.width = wid
        self.height = hg
        self.shwStdntsBttn = None
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Student.json") 

    def makeTable(self):
        holder = Frame(self.rt)
        self.my_tree = ttk.Treeview(holder)
        vscrl = ttk.Scrollbar(holder,orient="vertical",command=self.my_tree.yview)
        vscrl.pack(side='right',fill='y')
        self.my_tree.configure(yscrollcommand = vscrl.set)
        holder.pack()
        colTup = ("ID","Tên","Giới tính","Địa chỉ","Số điện thoại","Tháng","Tình trạng")
        self.my_tree['columns'] = colTup
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("ID",anchor=W,width=int(0.15*self.width))
        self.my_tree.column("Tên",anchor=E,width=int(0.15*self.width))
        self.my_tree.column("Giới tính",anchor=W,width=int(0.12*self.width))
        self.my_tree.column("Địa chỉ",anchor=W,width=int(0.18*self.width))
        self.my_tree.column("Số điện thoại",anchor=W,width=int(0.18*self.width))
        self.my_tree.column("Tháng",anchor=W,width=int(0.12*self.width))
        self.my_tree.column("Tình trạng",anchor=E,width=int(0.1*self.width))
        for i in range(0,len(colTup)):
            anch = CENTER
            self.my_tree.heading(colTup[i],text=colTup[i],anchor=anch)

    def fillTable(self): 
        x = self.my_tree.get_children() 
        if x != '()':
            for child in x:
                self.my_tree.delete(child)    
        fl = ""
        try:
            fl = open(self.dataFile,"r")
        except IOError:
            mssg = messagebox.showerror('Lỗi','JSON data file not found')
            return
        data = json.load(fl)
        lst = data["Students"]
        for i in range(0,len(lst)):
            self.my_tree.insert(parent='', index='end', iid=i, text="", values=(lst[i]["Rollno"],lst[i]["Name"],
                                                                                lst[i]["Gender"],lst[i]["address"],
                                                                                lst[i]["Phone no"],lst[i]["Batch"],
                                                                                lst[i]["Hostel"]))
            
    def shwStd(self):
        self.fillTable()

    def shwBttn(self):
        def on_enter(e):
            self.shwStdntsBttn['activebackground'] = "black"
            self.shwStdntsBttn["activeforeground"] = "white"
        def on_click(e):
            self.shwStdntsBttn['activebackground'] = "white"
            self.shwStdntsBttn["activeforeground"] = "black"      
        def on_release(e):
            self.shwStdntsBttn['activebackground'] = "black"
            self.shwStdntsBttn["activeforeground"] = "white"        
        self.shwStdntsBttn = Button(self.rt, text="Hiển thị học sinh", bg="black",fg="white",command=self.shwStd)
        self.shwStdntsBttn.bind('<Enter>',on_enter)
        self.shwStdntsBttn.bind('<Button-1>',on_click)
        self.shwStdntsBttn.bind('<ButtonRelease-1>',on_release)
        self.shwStdntsBttn.place(relx=0.5,rely=0.8,anchor=CENTER)  
        
    def dispStdnt(self):
        self.makeTable()
        self.shwBttn()
        self.my_tree.pack()
        
        
