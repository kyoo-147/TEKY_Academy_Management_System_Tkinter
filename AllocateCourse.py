# -*- coding: utf-8 -*-
# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

import sys
from os import path
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import json
from tkinter.filedialog import asksaveasfile

class allocCourse():
    def __init__(self,window,wid,hg):
        self.rt = window
        self.width = wid
        self.height = hg
        self.eStRll = ""
        self.eCrsName = ""
        proj_folder = path.dirname(__file__)
        data_folder = path.join(proj_folder,'data')
        self.CourseFile = path.join(data_folder,"Course.json") 
        self.StudentFile = path.join(data_folder,"Student.json")
        self.dataFile = path.join(data_folder,"Allocation.json") 
        self.readCourseJSON()

    def readCourseJSON(self): 
        try:
            self.reader = open(self.CourseFile,"r")
            self.CourseData = json.load(self.reader)
            self.CrsList = self.CourseData["Courses"]
            self.reader = open(self.StudentFile,"r")
            self.StudentData = json.load(self.reader)
            self.StuList = self.StudentData["Students"]            
        except:
            msg = messagebox.showerror("Error","JSON files not found")
            quit()

    def labels(self):
        fntStyle = tkFont.Font(size=12)
        lblList = []
        lblList.append(Label(self.rt,text="ID học sinh",font=fntStyle))
        lblList.append(Label(self.rt,text="Mã khóa học",font=fntStyle))
        self.eStRll = Entry(self.rt,width=int(self.width/23.4))
        self.crsName = StringVar()
        vlist = []
        for sub in self.CrsList:
            vlist.append(sub["CourseName"])
        self.eCrsName = ttk.Combobox(self.rt, width = int(self.width/23.4)-1, textvariable = self.crsName, values=vlist)
        yOffset = self.height/4.8 
        interval = self.height/4.8 
        xoff = self.width/2826.206896552 
        self.eStRll.place(anchor=NE, relx=0.8, y = yOffset)
        self.eCrsName.place(anchor=NE, relx=0.8, y = yOffset + interval)        
        for i in range(len(lblList)):
            lblList[i].place(anchor=NE, relx = xoff, y = (yOffset + (i * interval)))
            
    def wrtInJson(self,data,flName):
        with open(flName,'w') as f: 
            json.dump(data, f, indent=4)   

    def allocateCrs(self):
        inTheList = False 
        for ele in self.StuList:
            if ele["Rollno"] == self.eStRll.get(): 
                inTheList = True
                break
        if not inTheList: 
            msg = messagebox.showwarning("Cánh báo","Không nhận được mã ID")
            return
        msgBox = messagebox.showinfo("Phân bổ","Khóa học được phân bổ")
        c_id = 0
        roll = self.eStRll.get()
        for sub in self.CrsList:
            if self.eCrsName.get() == sub["CourseName"]:
                c_id = sub["CourseID"]
        nstds = {
            "Rollno": roll,
            "CourseID": c_id
        }
        fl = ""
        try:
            fl = open(self.dataFile,"r")
            details = json.load(fl)
            temp = details["Stu_Course"]
            temp.append(nstds)
            self.wrtInJson(details,self.dataFile)
        except IOError:
            fl = open(self.dataFile,"w")
            d = {
                "Stu_Course":[nstds]}
            json.dump(d,fl,indent=4)
        fl.close()

    def clearInput(self):
        self.eStRll.delete(0,'end')
        self.eCrsName.delete(0,'end')

    def svBttnHvr(self,e):
        self.svBtnLabel.config(text="Phân bổ khóa học",borderwidth=2,relief="ridge")

    def svBttnLv(self,e):
        self.svBtnLabel.config(text="",borderwidth=0,relief="flat")    
        
    def bttns(self):
        saveBttn = Button(self.rt,text="Phân bổ",command=self.allocateCrs,width=15)
        self.svBtnLabel = Label(self.rt,text=None)
        saveBttn.bind('<Enter>',self.svBttnHvr)
        saveBttn.bind('<Leave>',self.svBttnLv)
        clearBttn = Button(self.rt,text="Xóa",command=self.clearInput,width=15)
        self.svBtnLabel.place(anchor=NE,relx=0.35,y=int(self.height/1.28)+20)
        clearBttn.place(anchor=NE,relx=0.8,y=int(self.height/1.28))
        saveBttn.place(anchor=NE,relx=0.4,y=int(self.height/1.28))