from tkinter import *
from tkinter import ttk
from NewStudent import *      
from Display import *           
from CourseCreate import *      
from DisplayCourse import *    
from AllocateCourse import *    
import tkinter as tk

class Game():
   def __init__(self):
      self.root = Tk()
      self.WIDTH = self.root.winfo_screenwidth() 
      self.HEIGHT = self.root.winfo_screenheight() 
      self.createWindow()

   def createWindow(self):
      try:
         self.root.attributes("-zoomed", True)
      except:
         self.root.geometry("%dx%d" % (self.WIDTH, self.HEIGHT))
      self.root.configure(bg="black")  
      self.root.title("Hệ thống đăng ký học sinh")
      self.root.resizable(False, False)
      title_font = ("Helvetica", 24, "bold")
      self.WorkH = int(2.5 * (self.HEIGHT / 5))
      self.WorkW = int(3 * (self.WIDTH / 5))
      self.root.minsize((self.WorkW + int(self.WorkW / 10)), self.HEIGHT - 40)
      title_label = tk.Label(self.root, text="", font=title_font, bg="#c3e6c3")
      title_label.pack(pady=55)

   def fillRootWindow(self):
      self.img1 = tk.PhotoImage(file="img\elogo.png")
      iLabel1 = tk.Label(self.root, image=self.img1, relief="flat")
      iLabel1.place(x=10, y=10)

      self.img2 = tk.PhotoImage(file="img\clogo.png")
      iLabel2 = tk.Label(self.root, image=self.img2, relief="flat")
      iLabel2.place(relx=1, y=5, anchor=tk.NE)

      self.img3 = tk.PhotoImage(file="img\plogo.png")
      iLabel3 = tk.Label(self.root, image=self.img3, relief="flat")
      iLabel3.place(relx=0.03, rely=0.5, anchor=tk.W)
      title_font = ("Times New Roman", 30, "bold")
      middle_font = ("Times", 25,"bold")
      label_font = ("Arial", 20, "bold")
      self.root.configure(bg="#88d498")
      chktUni = tk.Label(self.root, text="HỌC VIỆN TEKY", bg="#c3e6c3", fg="black", font=title_font)
      chktUni.place(relx=0.5, rely=0.05, anchor=tk.N)
      stuMgm = tk.Label(self.root, text="Dữ liệu học sinh", bg="#c3e6c3", fg="black", font=middle_font)
      stuMgm.place(relx=0.5, rely=0.2, anchor=tk.S)
      dataStorage = tk.Label(self.root, text="Hệ Thống Lưu Trữ Dữ Liệu Học Sinh", bg="#c3e6c3", fg="black", font=label_font)
      dataStorage.place(relx=0.5, rely=0.92, anchor=tk.S)
      self.mainFrame = tk.Frame(self.root, height=self.WorkH, width=self.WorkW, bg="white")
      self.mainFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

   def makeTabView(self):
      tabW = self.WorkW
      tabH = self.WorkH
      nBook = ttk.Notebook(self.mainFrame, style='Custom.TNotebook')
      nBook.pack(padx=10, pady=10)
      new_student = Frame(nBook, width=tabW, height=tabH, bg='sky blue') 
      nBook.add(new_student, text='Học sinh mới')
      nS = nStudent(new_student, self.WorkW, self.WorkH)
      nS.labels()
      nS.bttns()
      display_st_info = Frame(nBook, width=tabW, height=tabH, bg='sky blue') 
      nBook.add(display_st_info, text='Hiển thị học sinh')
      disp = Disp(display_st_info, self.WorkW, self.WorkH)
      disp.dispStdnt()
      createCourse = Frame(nBook, width=tabW, height=tabH, bg='sky blue')  
      nBook.add(createCourse, text='Tạo khóa học')
      nC = nCourse(createCourse, self.WorkW, self.WorkH)
      nC.labels()
      nC.bttns()
      display_crs = Frame(nBook, width=tabW, height=tabH, bg='sky blue')  
      nBook.add(display_crs, text='Hiển thị khóa học')
      dispCrs = DispCrs(display_crs, self.WorkW, self.WorkH)
      dispCrs.table()
      alloc_crs = Frame(nBook, width=tabW, height=tabH, bg='sky blue') 
      nBook.add(alloc_crs, text='Phân bổ khóa học')
      allocateCrs = allocCourse(alloc_crs, self.WorkW, self.WorkH)
      allocateCrs.labels()
      allocateCrs.bttns()
      style = ttk.Style()
      style.configure('Custom.TNotebook.Tab', padding=[10, 5], font=('Helvetica', '12', 'bold'))
      nBook.pack_propagate(0)

   def gameLoop(self):
      self.fillRootWindow() 
      self.makeTabView() 
      self.root.mainloop() 
      
G = Game() 
G.gameLoop() 