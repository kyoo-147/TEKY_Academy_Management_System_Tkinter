# -*- coding: utf-8 -*-
# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

from os import path
from tkinter import *
from tkinter import ttk, messagebox
import json

class DispCrs():
    def __init__(self,window,wid,hg):
        self.rt = window
        self.width = wid
        self.height = hg
        self.shwCrsBttn = None
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Course.json")      

    def makeTable(self):
        self.my_tree = ttk.Treeview(self.rt)
        colTup = ("CourseID","CourseName")
        self.my_tree['columns'] = colTup
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("CourseID",anchor=W,width=int(0.25*(self.width/2)),minwidth=75)
        self.my_tree.column("CourseName",anchor=E,width=int(0.75*(self.width/2)))
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
            mssg = messagebox.showerror('Lỗi','Không tìm thấy dữ liệu')
            return
        data = json.load(fl)
        lst = data["Courses"]
        
        for i in range(0,len(lst)):
            self.my_tree.insert(parent='', index='end', iid=i, text="", values=(lst[i]["CourseID"],lst[i]["CourseName"]))

    def shwStd(self):
        self.fillTable()

    def shwBttn(self):
        def on_enter(e):
            self.shwCrsBttn['activebackground'] = "black"
            self.shwCrsBttn["activeforeground"] = "white"
        def on_click(e):
            self.shwCrsBttn['activebackground'] = "white"
            self.shwCrsBttn["activeforeground"] = "black"      
        def on_release(e):
            self.shwCrsBttn['activebackground'] = "black"
            self.shwCrsBttn["activeforeground"] = "white"     
        self.shwCrsBttn = Button(self.rt, text="Xem khóa học", bg="black",fg="white",command=self.shwStd)
        self.shwCrsBttn.bind('<Enter>',on_enter)
        self.shwCrsBttn.bind('<Button-1>',on_click)
        self.shwCrsBttn.bind('<ButtonRelease-1>',on_release)
        self.shwCrsBttn.place(relx=0.5,rely=0.8,anchor=CENTER)
            
    def table(self):
        self.makeTable()
        self.shwBttn()
        self.my_tree.pack()