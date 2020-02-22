from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from glcm4sudut import glcm4s
from itung import knn
import numpy as np

class gui:    
    def __init__(self, ini):
        data = "3.png"
        text11 = "0"
        text12 = "0"
        text13 = "0"
        text14 = "0"
        text21 = "0"
        text22 = "0"
        text23 = "0"
        text24 = "0"
        text31 = "0"
        text32 = "0"
        text33 = "0"
        text34 = "0"
        text41 = "0"
        text42 = "0"
        text43 = "0"
        text44 = "0"

        gambar = ""
        
        self.ini = ini
        self.initUI()
        var = StringVar()

        self.lbllist = Label(ini, text="HASIL PERHITUNGAN KNN").grid(row=7, column=0, columnspan=3)
        
        self.table()
        self.tombol(NORMAL,DISABLED)
        self.gmr(data)
        self.kualifikasi(text11, text12, text13, text14,
        text21, text22, text23, text24,
        text31, text32, text33, text34,
        text41, text42, text43, text44)

    def tombol(self, statusU, statusP):
        self.buttonUpload = Button(text="UPLOAD", width=6, command=self.upload, state=statusU)
        self.buttonUpload.grid(row=6, column=0, columnspan=2)

        self.buttonProses = Button(text="PROSES", width=6, command=self.hitung, state=statusP).grid(row=6, column=3, columnspan=2)

    def kualifikasi(self,
    text11,text12,text13,text14,
    text21,text22,text23,text24,
    text31,text32,text33,text34,
    text41,text42,text43,text44):
        self.lFJ1 = Label( text="Energy").grid(row=0, column=3)
        self.lFJ2 = Label( text="Homogen").grid(row=0, column=4)
        self.lFJ3 = Label( text="Contrast").grid(row=0, column=5)
        self.lFJ4 = Label( text="Correlation").grid(row=0, column=6)
        self.lF1 = Label( text="1").grid(row=1, column=2)
        lebar = 9
        self.lF11 = Label( width=lebar, bg="white", text=text11 ).grid(row=1, column=3)
        self.lF12 = Label( width=lebar, bg="white", text=text12 ).grid(row=1, column=4)
        self.lF13 = Label( width=lebar, bg="white", text=text13 ).grid(row=1, column=5)
        self.lF14 = Label( width=lebar, bg="white", text=text14 ).grid(row=1, column=6)
        
        self.lF2 = Label( text="2").grid(row=2, column=2)
        self.lF21 = Label( width=lebar, bg="white", text=text21 ).grid(row=2, column=3)
        self.lF22 = Label( width=lebar, bg="white", text=text22 ).grid(row=2, column=4)
        self.lF23 = Label( width=lebar, bg="white", text=text23 ).grid(row=2, column=5)
        self.lF24 = Label( width=lebar, bg="white", text=text24 ).grid(row=2, column=6)
        
        self.lF3 = Label( text="3").grid(row=3, column=2)
        self.lF31 = Label( width=lebar, bg="white", text=text31 ).grid(row=3, column=3)
        self.lF32 = Label( width=lebar, bg="white", text=text32 ).grid(row=3, column=4)
        self.lF33 = Label( width=lebar, bg="white", text=text33 ).grid(row=3, column=5)
        self.lF34 = Label( width=lebar, bg="white", text=text34 ).grid(row=3, column=6)
        
        self.lF4 = Label( text="4").grid(row=4, column=2)
        self.lF41 = Label( width=lebar, bg="white", text=text41 ).grid(row=4, column=3)
        self.lF42 = Label( width=lebar, bg="white", text=text42 ).grid(row=4, column=4)
        self.lF42 = Label( width=lebar, bg="white", text=text43 ).grid(row=4, column=5)
        self.lF42 = Label( width=lebar, bg="white", text=text44 ).grid(row=4, column=6)


    def gmr(self, data):
        img=Image.open(data)
        self.tkimage = ImageTk.PhotoImage(img)
        self.lblimage = Label(image=self.tkimage, width=70, height=70).grid(row=0, column=0, rowspan=5, columnspan =2)
    
    def initUI(self):
        self.ini.title("PERTHITUNGAN GLCM 4 SUDUT")
        self.ini.geometry("1250x300")
   
    def upload(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("gambar files","*.bmp"),("all files","*.*")))
        gambar = str(filename)
        self.gmr(gambar)
        self.img = glcm4s(gambar)
        self.img.glcm()
        text11 = round(self.img.data[0],4)
        text12 = round(self.img.data[1],4)
        text13 = round(self.img.data[2],4)
        text14 = round(self.img.data[3],4)
        text21 = round(self.img.data[4],4)
        text22 = round(self.img.data[5],4)
        text23 = round(self.img.data[6],4)
        text24 = round(self.img.data[7],4)
        text31 = round(self.img.data[8],4)
        text32 = round(self.img.data[9],4)
        text33 = round(self.img.data[10],4)
        text34 = round(self.img.data[11],4)
        text41 = round(self.img.data[12],4)
        text42 = round(self.img.data[13],4)
        text43 = round(self.img.data[14],4)
        text44 = round(self.img.data[15],4)
        self.kualifikasi(text11,text12,text13,text14,
        text21,text22,text23,text24,
        text31,text32,text33,text34,
        text41,text42,text43,text44)
        self.tombol(DISABLED,NORMAL)

    def hitung(self):
        result = knn([self.img.data])

        baris = 9
        lebar = 9
        for data in range(3):
            kolom = 0
            for D in range(18):
                if D == 16:
                    a = result.list[data][D]
                else:
                    a = round(result.list[data][D],4)
                b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1
        self.tombol(NORMAL, DISABLED)
    
    def table(self):
        baris = 9
        lebar = 9
        
        a = "Energy1"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 0)
        
        a = "Homogen1"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 1)
        
        a = "Contrast1"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 2)
        
        a = "Corr1"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 3)
        
        a = "Energy2"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 4)
        
        a = "Homogen2"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 5)
        
        a = "Contrast2"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 6)
        
        a = "Corr2"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 7)
        
        a = "Energy3"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 8)
        
        a = "Homogen3"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 9)
        
        a = "Contrast3"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 10)
        
        a = "Corr3"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 11)
        
        a = "Energy4"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 12)
        
        a = "Homogen4"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 13)
        
        a = "Contrast4"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 14)
        
        a = "Corr4"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 15)
        
        a = "Label"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 16)
        
        a = "Dist"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 17)
        
        for data in range(3):
            kolom = 0
            for D in range(18):
                a = "-"
                b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1

root = Tk()
app = gui(root)
root.mainloop()
