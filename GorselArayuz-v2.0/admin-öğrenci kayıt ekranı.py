import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql


root = tk.Tk()
root.title("Kayıt")
width = 800
height = 900
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


headingLabel = Label(headingFrame1, text="Öğrenci Kayıt Ekranı", bg='black', fg='white', font=('Courier', 20))
headingLabel.place(x=0, y=0, width=590, height=40)


#arkplan2
labelFrame = Frame(root, bg='black')
labelFrame.place(x=100, y=100, width=600, height=750)


# TC
lb1 = Label(labelFrame, text="TC Kimlik Numarası : ", bg='black', fg='white', font=('Courier', 11))
lb1.place(x=0, y=10, height=10)

ogrenci= Entry(labelFrame)
ogrenci.place(x=200, y=10, width=300, height=20)


# Numara
lb2 = Label(labelFrame, text="Öğrenci Numarası: ", bg='black', fg='white', font=('Courier', 11))
lb2.place(x=0, y=50, height=10)

ogrenci2 = Entry(labelFrame)
ogrenci2.place(x=200, y=50, width=300, height=20)

# Adı
lb3 = Label(labelFrame, text="Öğrenci Adı: ", bg='black', fg='white', font=('Courier', 11))
lb3.place(x=0, y=90, height=15)

ogrenci3= Entry(labelFrame)
ogrenci3.place(x=200, y=90, width=300, height=20)


# Soyadı
lb4 = Label(labelFrame, text="Öğrenci Soyadı : ", bg='black', fg='white', font=('Courier', 11))
lb4.place(x=0, y=130, height=15)

ogrenci4= Entry(labelFrame)
ogrenci4.place(x=200, y=130, width=300, height=20)



# Cinsiyet
lb5 = Label(labelFrame, text="Cinsiyet: ", bg='black', fg='white', font=('Courier', 11))
lb5.place(x=0, y=170, height=15)

n = tk.StringVar()
ogrenci5 = ttk.Combobox(labelFrame, textvariable=n, values = ('KIZ', 'ERKEK'))
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


# Sınav Notları
lb8 = Label(labelFrame, text="SINAV NOTLARI ", bg='black', fg='white', font=('Courier', 11))
lb8.place(x=0, y=300, height=15)


#Dersler
lb8 = Label(labelFrame, text="Türkçe : ", bg='black', fg='white', font=('Courier', 11))
lb8.place(x=0, y=330, height=15)

ogrenci8 = Entry(labelFrame)
ogrenci8.place(x=200, y=330, width=50, height=20)

# Matematik
lb9 = Label(labelFrame, text="Matematik : ", bg='black', fg='white', font=('Courier', 11))
lb9.place(x=0, y=360, height=15)

ogrenci9 = Entry(labelFrame)
ogrenci9.place(x=200, y=360, width=50, height=20)

# Fen Bilimleri
lb10 = Label(labelFrame, text="Fen Bilimleri : ", bg='black', fg='white', font=('Courier', 11))
lb10.place(x=0, y=390, height=15)

ogrenci10 = Entry(labelFrame)
ogrenci10.place(x=200, y=390, width=50, height=20)

# Sosyal Bilgiler
lb11 = Label(labelFrame, text="Sosyal Bilgiler : ", bg='black', fg='white', font=('Courier', 11))
lb11.place(x=0, y=420, height=15)

ogrenci11 = Entry(labelFrame)
ogrenci11.place(x=200, y=420, width=50, height=20)

# İngilizce
lb11 = Label(labelFrame, text="İngilizce : ", bg='black', fg='white', font=('Courier', 11))
lb11.place(x=0, y=450, height=15)

ogrenci11 = Entry(labelFrame)
ogrenci11.place(x=200, y=450, width=50, height=20)

# Resim
lb12 = Label(labelFrame, text="Resim : ", bg='black', fg='white', font=('Courier', 11))
lb12.place(x=0, y=480, height=15)

ogrenci12 = Entry(labelFrame)
ogrenci12.place(x=200, y=480, width=50, height=20)

# Müzik
lb13 = Label(labelFrame, text="Müzik : ", bg='black', fg='white', font=('Courier', 11))
lb13.place(x=0, y=510, height=15)

ogrenci13 = Entry(labelFrame)
ogrenci13.place(x=200, y=510, width=50, height=20)

# Beden Eğitimi
lb14 = Label(labelFrame, text="Beden Eğitimi : ", bg='black', fg='white', font=('Courier', 11))
lb14.place(x=0, y=540, height=15)

ogrenci14 = Entry(labelFrame)
ogrenci14.place(x=200, y=540, width=50, height=20)

# Devamsızlık Bilgisi
lb15 = Label(labelFrame, text="Devamsızlık Bilgileri : ", bg='black', fg='white', font=('Courier', 11))
lb15.place(x=0, y=600, height=15)

# Özürlü
lb14 = Label(labelFrame, text="Özürlü Devamsız Gün Sayısı : ", bg='black', fg='white', font=('Courier', 11))
lb14.place(x=0, y=630, height=15)

ogrenci14 = Entry(labelFrame)
ogrenci14.place(x=280, y=630, width=50, height=20)

# Özürsüz
lb14 = Label(labelFrame, text="Özürsüz Devamsız Gün Sayısı : ", bg='black', fg='white', font=('Courier', 11))
lb14.place(x=0, y=660, height=15)

ogrenci14 = Entry(labelFrame)
ogrenci14.place(x=280, y=660, width=50, height=20)




# Butonlar
gonderBtn = Button(root, text="GÖNDER", bg='#d1ccc0', fg='black')
gonderBtn.place(x=200, y=860, width=60, height=30)

cikisBtn = Button(root, text="ÇIKIŞ", bg='#d1ccc0', fg='black',command=root.destroy)
cikisBtn.place(x=500, y=860, width=60, height=30)




root.mainloop()
