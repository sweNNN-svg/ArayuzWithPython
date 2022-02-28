import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

form = tk.Tk()
form.title("Öğrenci Bilgi Sistemi")

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


#sekme oluşturma
tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", secilitab)
tab_parent.add(tab1, text=" ADMIN ")
tab_parent.add(tab2, text=" OGRETMEN ")
tab_parent.add(tab3, text=" OGRENCI ")
tab_parent.add(tab4, text=" DESTEK ")





tab_parent.pack(expand=1, fill='both')
form.mainloop()
