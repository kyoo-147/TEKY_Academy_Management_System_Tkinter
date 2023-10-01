# -*- coding: utf-8 -*-
# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

from os import path
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import json

class nStudent(): 
    def __init__(self,window,wid,hg):
        self.rt = window 
        self.width = wid
        self.height = hg
        self.eyName = ""
        self.eyRll = ""
        self.chGender = ""
        self.AoC = ""
        self.phN = ""
        self.yrB = ""
        self.Hstl = ""
        self.svBtnLabel = ""
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.dataFile = path.join(data_folder,"Student.json")

    def labels(self):
        fntStyle = tkFont.Font(size=12)
        lblList = []
        lblList.append(Label(self.rt,text="Nhập tên của bạn",font=fntStyle))
        lblList.append(Label(self.rt,text="Nhập ID",font=fntStyle))
        lblList.append(Label(self.rt,text="Chọn giới tính",font=fntStyle))
        lblList.append(Label(self.rt,text="Địa chỉ liên lạc",font=fntStyle))
        lblList.append(Label(self.rt,text="Số điện thoại",font=fntStyle))
        lblList.append(Label(self.rt,text="Tháng nhập học",font=fntStyle))
        lblList.append(Label(self.rt,text="Kiểm tra tình trạng nhập học",font=fntStyle))
        self.eyName = Entry(self.rt,width=int(self.width/23.4))
        self.eyRll = Entry(self.rt,width=int(self.width/23.4)) 
        self.chGender = StringVar()
        self.radioMl = Radiobutton(self.rt, text="Nam", variable=self.chGender, value="Male")
        self.radioFml = Radiobutton(self.rt, text="Nữ", variable=self.chGender, value="Female")
        self.chGender.set(0)
        self.AoC = Entry(self.rt,width=int(self.width/23.4))
        self.phN = Entry(self.rt,width=int(self.width/23.4)) 
        self.yrB = StringVar()
        vlist = ["Tháng 1","Tháng 2","Tháng 3","Tháng 4","Tháng 5","Tháng 6","Tháng 7","Tháng 8","Tháng 9","Tháng 10","Tháng 11","Tháng 12"]
        self.batchCombo = ttk.Combobox(self.rt, width = int(self.width/41), textvariable = self.yrB, values=vlist)
        self.Hstl = StringVar()
        self.chkBox = Checkbutton(self.rt, text='Đang học',variable=self.Hstl, onvalue=True, offvalue=False)
        self.chkBox.deselect()
        yOffset = self.height/19.2 
        interval = self.height/9.6 
        xoff = self.width/2826.206896552 
        self.eyName.place(anchor=NW, relx=0.72, y = yOffset)
        self.eyRll.place(anchor=NW, relx=0.72, y = yOffset + interval)
        self.radioMl.place(anchor=NW, relx=0.72, y = yOffset + 2 * interval)
        self.radioFml.place(anchor=NE, relx=1, y = yOffset + 2 * interval)
        self.AoC.place(anchor=NW, relx=0.72, y = yOffset + 3 * interval)
        self.phN.place(anchor=NW, relx=0.72, y = yOffset + 4 * interval)
        self.batchCombo.place(anchor=NE, relx=1, y = yOffset + 5 * interval)
        self.chkBox.place(anchor=NE, relx=1, y = yOffset + 6 * interval)
        for i in range(len(lblList)):
            lblList[i].place(anchor=NE, relx = xoff, y = (yOffset + (i * interval)))

    def wrtInJson(self,data,flName):
        with open(flName,'w') as f:
            json.dump(data, f, indent=4)

    def saveFile(self): 
        hstl = False
        if self.Hstl.get() == '1':
            hstl = True
        nstds = {
            "Rollno": self.eyRll.get(),
            "Name": self.eyName.get(),
            "Gender": self.chGender.get(),
            "address": self.AoC.get(),
            "Phone no": self.phN.get(),
            "Batch": self.yrB.get(),
            "Hostel": hstl
        }        
        fl = ""
        try: 
            fl = open(self.dataFile,"r") 
            details = json.load(fl)
            temp = details["Students"]
            temp.append(nstds)
            self.wrtInJson(details,self.dataFile) 
        except IOError: 
            fl = open(self.dataFile,"w")
            d = {
                "Students":[nstds]}
            json.dump(d,fl,indent=4)
        fl.close()
        msgBox = messagebox.showinfo("Lưu","Hồ sơ của bạn đã được lưu") 
        self.clearInput()

    def clearInput(self): 
        self.eyName.delete(0,'end')
        self.eyRll.delete(0,'end')
        self.AoC.delete(0,'end')
        self.phN.delete(0,'end')
        self.chGender.set(0)
        self.batchCombo.delete(0,'end')
        self.chkBox.deselect()

    def svBttnHvr(self,e):
        self.svBtnLabel.config(text="Lưu bản ghi",borderwidth=2,relief="ridge")
        self.svBtnLabel.place(anchor=NE,relx=0.46,y=int(self.height/1.28)+25)

    def svBttnLv(self,e):
        self.svBtnLabel.config(text="",borderwidth=0,relief="flat")    
        self.svBtnLabel.place(anchor=NE,relx=0,y=int(self.height/1.28)+25)
        
    def bttns(self):
        saveBttn = Button(self.rt,text="Lưu",command=self.saveFile,width=15)
        self.svBtnLabel = Label(self.rt,text=None)
        saveBttn.bind('<Enter>',self.svBttnHvr)
        saveBttn.bind('<Leave>',self.svBttnLv)
        clearBttn = Button(self.rt,text="Xóa",command=self.clearInput,width=15)
        clearBttn.place(anchor=NE,relx=0.65,y=int(self.height/1.28))
        saveBttn.place(anchor=NE,relx=0.47,y=int(self.height/1.28))
        
