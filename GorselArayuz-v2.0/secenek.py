from tkinter import *
from tkinter import messagebox



root = Tk()
root.title("Anime")
root.minsize(width=400, height=400)
root.geometry("700x600")
same = True
n = 0.25


######################################################################

Canvas1 = Canvas(root)


headingFrame1 = Frame(root, bg="#5211D4", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Kayıt Ekranı", bg='black', fg='white',
                     font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Öğretmen Kaydı", bg='black', fg='white')
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Öğrenci Kaydı", bg='black', fg='white')
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Kaytıları Görüntüle", bg='black', fg='white')
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Çıkış", bg='black', fg='white', command=root.destroy)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
