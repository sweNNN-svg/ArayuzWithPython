import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql


root = tk.Tk()
root.title("Kayıt")
width = 800
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#arkplan1
Canvas1 = Canvas(root)

Canvas1.config(bg="#180750")
Canvas1.pack(expand=True, fill=BOTH)

#başlık
headingFrame1 = Frame(root, bg="#260EAF", bd=5)
headingFrame1.place(x=100, y=10, width=600, height=50)


headingLabel = Label(headingFrame1, text="Öğretmen Kayıt Ekranı", bg='black', fg='white', font=('Courier', 20))
headingLabel.place(x=0, y=0, width=590, height=40)


#arkplan2
labelFrame = Frame(root, bg='black')
labelFrame.place(x=100, y=100, width=600, height=350)


# TC
lb1 = Label(labelFrame, text="TC Kimlik Numarası : ", bg='black', fg='white', font=('Courier', 11))
lb1.place(x=0, y=10, height=10)

ogrenci= Entry(labelFrame)
ogrenci.place(x=200, y=10, width=300, height=20)


# Numara
lb2 = Label(labelFrame, text="Öğretmen Şifresi: ", bg='black', fg='white', font=('Courier', 11))
lb2.place(x=0, y=50, height=10)

ogrenci2 = Entry(labelFrame)
ogrenci2.place(x=200, y=50, width=300, height=20)

# Adı
lb3 = Label(labelFrame, text="Öğretmen Adı: ", bg='black', fg='white', font=('Courier', 11))
lb3.place(x=0, y=90, height=15)

ogrenci3= Entry(labelFrame)
ogrenci3.place(x=200, y=90, width=300, height=20)


# Soyadı
lb4 = Label(labelFrame, text="Öğretmen Soyadı : ", bg='black', fg='white', font=('Courier', 11))
lb4.place(x=0, y=130, height=15)

ogrenci4= Entry(labelFrame)
ogrenci4.place(x=200, y=130, width=300, height=20)



# Cinsiyet
lb5 = Label(labelFrame, text="Cinsiyet: ", bg='black', fg='white', font=('Courier', 11))
lb5.place(x=0, y=170, height=15)

n = tk.StringVar()
ogrenci5 = ttk.Combobox(labelFrame, textvariable=n, values = ('KADIN', 'ERKEK'))
ogrenci5.place(x=200, y=170, width=300, height=20)


# İletişim bilgileri
lb6 = Label(labelFrame, text="Adres : ", bg='black', fg='white', font=('Courier', 11))
lb6.place(x=0, y=210, height=15)

ogrenci6 = Entry(labelFrame)
ogrenci6.place(x=200, y=210, width=300, height=20)

lb7 = Label(labelFrame, text="Telefon Numrası : ", bg='black', fg='white', font=('Courier', 11))
lb7.place(x=0, y=250, height=15)

ogrenci7 = Entry(labelFrame)
ogrenci7.place(x=200, y=250, width=300, height=20)





# Butonlar
gonderBtn = Button(root, text="GÖNDER", bg='#d1ccc0', fg='black')
gonderBtn.place(x=200, y=400
                , width=60, height=30)

cikisBtn = Button(root, text="ÇIKIŞ", bg='#d1ccc0', fg='black',command=root.destroy)
cikisBtn.place(x=500, y=400, width=60, height=30)




root.mainloop()
