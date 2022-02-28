import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

form = tk.Tk()
form.title("Öğrenci Bilgi ")

form.geometry("500x500")

# VERİ TABANI İÇİN DEĞİŞKEN TANIMLAMALARI


visimtab1 = tk.StringVar()
vsoyadtab1 = tk.StringVar()
vunvantab1 = tk.StringVar()


visimtab2 = tk.StringVar()
vsoyadtab2 = tk.StringVar()
vunvantab2 = tk.StringVar()
 


def secilitab(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Tüm Kayıtlar":

        print("Tüm kayıtlar seçildi")

    if tab_text == "Yeni  Kayıt Ekle":

        print("Yeni  Kayıt Ekle seçildi")
    if tab_text == "Yardım":

        print("Yardım seçildi")


# SEKME OLUŞTURMA KISMI
tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", secilitab)
tab_parent.add(tab1, text="Tüm Kayıtlar")
tab_parent.add(tab2, text="Yeni Kayıt Ekle")
tab_parent.add(tab3, text="Yardım")
tab_parent.add(tab4, text="YBS")


# 1. TAB İÇİN NESNELER

yeni = tk.Label(tab4, text="TRABZON:")
yeni.grid(row=0, column=0, padx=15, pady=15)

isimetiket = tk.Label(tab1, text="Adınız:")
soyadetiket = tk.Label(tab1, text="Soyadınız:")
unvanetiket = tk.Label(tab1, text="Ünvanınız:")

buton1 = tk.Radiobutton(tab1)

isimgirdi = tk.Entry(tab1, textvariable=visimtab1)
soyadgirdi = tk.Entry(tab1,textvariable=vsoyadtab1)
unvangirdi = tk.Entry(tab1,textvariable=vunvantab1)



ileributon = tk.Button(tab1, text="İleri")
geributon = tk.Button(tab1, text="Geri")


# 1. TAB İÇİN NESNELERİN YERLEŞTİRİLMESİ

isimetiket.grid(row=0, column=0, padx=15, pady=15)
isimgirdi.grid(row=0, column=1, padx=15, pady=15)

soyadetiket.grid(row=1, column=0, padx=15, pady=15)
soyadgirdi.grid(row=1, column=1, padx=15, pady=15)

unvanetiket.grid(row=2, column=0, padx=15, pady=15)
unvangirdi.grid(row=2, column=1, padx=15, pady=15)

buton1.grid(row=3, column=0, padx=15, pady=15)


ileributon.grid(row=4, column=0, rowspan=3, padx=15, pady=15)

geributon.grid(row=4, column=2, rowspan=3, padx=15, pady=15)

# 2. TAB İÇİN NESNELER
isimetikettab2 = tk.Label(tab2, text="Adınız:")
soyadetikettab2 = tk.Label(tab2, text="Soyadınız:")
unvantab2 = tk.Label(tab2, text="Unvan:")

isimgirditab2 = tk.Entry(tab2,textvariable=visimtab2)
soyadıgirditab2= tk.Entry(tab2,textvariable=vsoyadtab2)
unvangirditab2 = tk.Entry(tab2,textvariable=vunvantab2)



uygulabuton = tk.Button(tab2, text="Bilgileri Veri tabanına ekle")

# 2. TAB İÇİN NESNELERİN YERLEŞTİRİLMESİ
isimetikettab2.grid(row=0, column=0, padx=15, pady=15)
isimgirditab2.grid(row=0, column=1, padx=15, pady=15)


soyadetikettab2.grid(row=1, column=0, padx=15, pady=15)
soyadıgirditab2.grid(row=1, column=1, padx=15, pady=15)

unvantab2.grid(row=2, column=0, padx=15, pady=15)
unvangirditab2.grid(row=2, column=1, padx=15, pady=15)

uygulabuton.grid(row=4, column=1, padx=15, pady=15)



tab_parent.pack(expand=1, fill='both')
form.mainloop()








