from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql





#silme ve çıkış fonksiyonu
def clear1():
	userentry1.delete(0,END)
	passentry1.delete(0,END)
def clear2():
	userentry2.delete(0,END)
	passentry2.delete(0,END)
def clear3():
	userentry3.delete(0,END)
	passentry3.delete(0,END)

def close():
	win.destroy()




#admin giriş fonksiyonu
	
def login1():
	if user_name1.get()=="" or password1.get()=="":
		messagebox.showerror("Hata","Kullanıcı Adınızı ve Şifrenizi Girin",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="ogrenci")
			cur = con.cursor()

			cur.execute("select * from admin where kullanici_adi=%s and sifre = %s",(user_name1.get(),password1.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Hata" , "Geçersiz Kullanıcı Adı ve Şifre", parent = win)

			else:
				messagebox.showinfo("Tamamdır!" , "Başarılı Bir Şekilde Giriş Yaptınız" , parent = win)
				close()
				secenek()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)
#öğretmen giriş fonksiyonu
def login2():
	if user_name2.get()=="" or password2.get()=="":
		messagebox.showerror("Hata","Kullanıcı Adınızı ve Şifrenizi Girin",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="ogrenci")
			cur = con.cursor()

			cur.execute("select * from ogretmen where tc=%s and ogretmen_sifresi = %s",(user_name2.get(),password2.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Hata" , "Geçersiz Kullanıcı Adı ve Şifre", parent = win)

			else:
				messagebox.showinfo("Tamamdır!" , "Başarılı Bir Şekilde Giriş Yaptınız" , parent = win)
				close()
				secenek2()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#öğrenci giriş fonksiyonu
def login3():
	if user_name3.get()=="" or password3.get()=="":
		messagebox.showerror("Hata","Kullanıcı Adınızı ve Şifrenizi Girin",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="ogrenci")
			cur = con.cursor()

			cur.execute("select * from ogrenci where tc=%s and ogrenci_numarasi = %s",(user_name3.get(),password3.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Hata" , "Geçersiz Kullanıcı Adı ve Şifre", parent = win)

			else:
				messagebox.showinfo("Tamamdır!" , "Başarılı Bir Şekilde Giriş Yaptınız" , parent = win)
				close()
				secenek3()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)
#######################################################################################
#admin seçenek ekranı
def  secenek():


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

                    btn1 = Button(root, text="Öğretmen Kaydı", bg='black', fg='white', command = ogretmenkayit)
                    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

                    btn2 = Button(root, text="Öğrenci Kaydı", bg='black', fg='white',command = ogrencikayit)
                    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

                    btn3 = Button(root, text="Kaytıları Görüntüle", bg='black', fg='white')
                    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

                    btn5 = Button(root, text="Çıkış", bg='black', fg='white', command=root.destroy)
                    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)





###veritabanı bağlantısı-ogretmen


def action():
                                tc = ogrt.get()
                                ogretmen_sifresi = ogrt2.get()
                                adi = ogrt3.get()
                                soyadi = ogrt4.get()
                                n1 = ogrt5.get()
                                adres = ogrt6.get()
                                telefon_numarasi = ogrt7.get()
                                
                                insertogretmen = "insert into "+ogretmenTable+" values ('"+tc+"','"+ogretmen_sifresi+"','"+adi+"','"+soyadi+"','"+n1+"','"+adres+"','"+telefon_numarasi+"')"
                                try:
                                        cur.execute(insertogretmen)
                                        con.commit()
                                        messagebox.showinfo('Başarılı!', "Öğretmen kaydı başarılı bir şekilde eklendi")
                                except:
                                        messagebox.showinfo("Hata!", "Veritabanına eklenemedi!")

def ogretmenkayit():

	global ogrt, ogrt2, ogrt3, ogrt4, ogrt5, ogrt6, ogrt7, ogretmenTable, con, cur, root
	
	con = pymysql.connect(
                            host="localhost",
                            user="root",
                            password="",
                            
                            database="ogrenci"
                            )
	cur = con.cursor()

	ogretmenTable = "ogretmen"



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

	# form data label
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

	ogrt= Entry(labelFrame)
	ogrt.place(x=200, y=10, width=300, height=20)


	# Numara
	lb2 = Label(labelFrame, text="Öğretmen Şifresi: ", bg='black', fg='white', font=('Courier', 11))
	lb2.place(x=0, y=50, height=10)

	ogrt2 = Entry(labelFrame)
	ogrt2.place(x=200, y=50, width=300, height=20)

	# Adı
	lb3 = Label(labelFrame, text="Öğretmen Adı: ", bg='black', fg='white', font=('Courier', 11))
	lb3.place(x=0, y=90, height=15)

	ogrt3= Entry(labelFrame)
	ogrt3.place(x=200, y=90, width=300, height=20)

	# Soyadı
	lb4 = Label(labelFrame, text="Öğretmen Soyadı : ", bg='black', fg='white', font=('Courier', 11))
	lb4.place(x=0, y=130, height=15)

	ogrt4= Entry(labelFrame)
	ogrt4.place(x=200, y=130, width=300, height=20)


	# Cinsiyet
	lb5 = Label(labelFrame, text="Cinsiyet: ", bg='black', fg='white', font=('Courier', 11))
	lb5.place(x=0, y=170, height=15)

	n1 = tk.StringVar()
	ogrt5 = ttk.Combobox(labelFrame, textvariable=n1, values = ('KADIN', 'ERKEK'))
	ogrt5.place(x=200, y=170, width=300, height=20)


	# İletişim bilgileri
	lb6 = Label(labelFrame, text="Adres : ", bg='black', fg='white', font=('Courier', 11))
	lb6.place(x=0, y=210, height=15)

	ogrt6 = Entry(labelFrame)
	ogrt6.place(x=200, y=210, width=300, height=20)

	lb7 = Label(labelFrame, text="Telefon Numrası : ", bg='black', fg='white', font=('Courier', 11))
	lb7.place(x=0, y=250, height=15)

	ogrt7 = Entry(labelFrame)
	ogrt7.place(x=200, y=250, width=300, height=20)

	# Butonlar

	gonderBtn = Button(root, text="GÖNDER", bg='#d1ccc0', fg='black', command = action)
	gonderBtn.place(x=200, y=400, width=60, height=30)

	cikisBtn = Button(root, text="ÇIKIŞ", bg='#d1ccc0', fg='black',command=root.destroy)
	cikisBtn.place(x=500, y=400, width=60, height=30)



#veritabanı bağlantısı
def action2():
                                tc = ogrenci.get()
                                ogrenci_numarasi= ogrenci2.get()
                                adi = ogrenci3.get()
                                soyadi = ogrenci4.get()
                                n2 = ogrenci5.get()
                                adres = ogrenci6.get()
                                telefon_numarasi = ogrenci7.get()
                                turkce = ogrenci8.get()
                                matematik = ogrenci9.get()
                                fen = ogrenci10.get()
                                sosyal = ogrenci11.get()
                                ingilizce = ogrenci12.get()
                                resim = ogrenci13.get()
                                muzik = ogrenci14.get()
                                beden = ogrenci15.get()
                                ozurlu = ogrenci16.get()
                                ozursuz = ogrenci17.get()
                                
                                
                                insertogrenci = "insert into "+ogrenci_bilgiTable+" values ('"+tc+"','"+ogrenci_numarasi+"','"+adi+"','"+soyadi+"','"+n2+"','"+adres+"','"+telefon_numarasi+"')"
                                try:
                                        cur.execute(insertogrenci)
                                        con.commit()
                                        messagebox.showinfo('Başarılı!', "Öğrenci kaydı başarılı bir şekilde eklendi")
                                except:
                                        messagebox.showinfo("Hata!", "Veritabanına eklenemedi!")



#öğrenci kayit
def ogrencikayit():

                            global ogrenci, ogrenci2, ogrenci3, ogrenci4, ogrenci5, ogrenci6, ogrenci7, ogrenci8, ogrenci9, ogrenci10, ogrenci11, ogrenci12, ogrenci13, ogrenci14, ogrenci15, ogrenci16, ogrenci17, con, cur, root, ogrenci_bilgiTable
                            

                            con = pymysql.connect(
                                    host="localhost",
                                    user="root",
                                    password="",
                                    database="ogrenci"
                                    )
                            cur = con.cursor()

                            ogrenci_bilgiTable = "ogrenci_bilgi"


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

                            n2 = tk.StringVar()
                            ogrenci5 = ttk.Combobox(labelFrame, textvariable=n2, values = ('KIZ', 'ERKEK'))
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
                            lb9 = Label(labelFrame, text="Türkçe : ", bg='black', fg='white', font=('Courier', 11))
                            lb9.place(x=0, y=330, height=15)

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

                            ogrenci12 = Entry(labelFrame)
                            ogrenci12.place(x=200, y=450, width=50, height=20)

                            # Resim
                            lb12 = Label(labelFrame, text="Resim : ", bg='black', fg='white', font=('Courier', 11))
                            lb12.place(x=0, y=480, height=15)

                            ogrenci13 = Entry(labelFrame)
                            ogrenci13.place(x=200, y=480, width=50, height=20)

                            # Müzik
                            lb13 = Label(labelFrame, text="Müzik : ", bg='black', fg='white', font=('Courier', 11))
                            lb13.place(x=0, y=510, height=15)

                            ogrenci14 = Entry(labelFrame)
                            ogrenci14.place(x=200, y=510, width=50, height=20)

                            # Beden Eğitimi
                            lb14 = Label(labelFrame, text="Beden Eğitimi : ", bg='black', fg='white', font=('Courier', 11))
                            lb14.place(x=0, y=540, height=15)

                            ogrenci15 = Entry(labelFrame)
                            ogrenci15.place(x=200, y=540, width=50, height=20)

                            # Devamsızlık Bilgisi
                            lb15 = Label(labelFrame, text="Devamsızlık Bilgileri : ", bg='black', fg='white', font=('Courier', 11))
                            lb15.place(x=0, y=600, height=15)

                            # Özürlü
                            lb14 = Label(labelFrame, text="Özürlü Devamsız Gün Sayısı : ", bg='black', fg='white', font=('Courier', 11))
                            lb14.place(x=0, y=630, height=15)

                            ogrenci16 = Entry(labelFrame)
                            ogrenci16.place(x=280, y=630, width=50, height=20)

                            # Özürsüz
                            lb14 = Label(labelFrame, text="Özürsüz Devamsız Gün Sayısı : ", bg='black', fg='white', font=('Courier', 11))
                            lb14.place(x=0, y=660, height=15)

                            ogrenci17 = Entry(labelFrame)
                            ogrenci17.place(x=280, y=660, width=50, height=20)




                            # Butonlar
                            gonderBtn = Button(root, text="GÖNDER", bg='#d1ccc0', fg='black', command = action2 )
                            gonderBtn.place(x=200, y=860, width=60, height=30)

                            cikisBtn = Button(root, text="ÇIKIŞ", bg='#d1ccc0', fg='black',command=root.destroy)
                            cikisBtn.place(x=500, y=860, width=60, height=30)

######################################################################################
#öğretmen seçenek ekranı
def  secenek2():


                    root = Tk()
                    root.title("Not/Devamsızlık")
                    root.minsize(width=400, height=400)
                    root.geometry("700x600")
                    same = True
                    n = 0.25


                    ######################################################################

                    Canvas1 = Canvas(root)


                    headingFrame1 = Frame(root, bg="#5211D4", bd=5)
                    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

                    headingLabel = Label(headingFrame1, text="Not/Devamsızlık Kayıt Ekranı", bg='black', fg='white',
                                         font=('Courier', 15))
                    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

                    btn1 = Button(root, text="Not/Devamsızlık Kayıt", bg='black', fg='white', command = notkayit)
                    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

                    btn2 = Button(root, text="Kayıtları Görüntüle", bg='black', fg='white',command = ogrencikayit)
                    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)


                    btn5 = Button(root, text="Çıkış", bg='black', fg='white', command=root.destroy)
                    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


#öğretmen notkaydı-edvamsızlık kaydı

def notkayit():
    
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

#####################################################################################
#öğrenci kayıt görüntüleme ekranı

def secenek3():

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

                    headingLabel = Label(headingFrame1, text="Not/Devamsızlık Bilgi Ekranı", bg='black', fg='white',
                                         font=('Courier', 15))
                    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

                    btn1 = Button(root, text="Ders Notlarını Görüntüle", bg='black', fg='white', command = ogretmenkayit)
                    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

                    btn2 = Button(root, text="Devamsızlıkları Görüntüle", bg='black', fg='white',command = ogrencikayit)
                    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

                    btn5 = Button(root, text="Çıkış", bg='black', fg='white', command=root.destroy)
                    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

























#login window
win = tk.Tk()

# app title
win.title("Docter Appointment App")

# window size
win.geometry("500x500")

#sekme oluşturma
tab_parent = ttk.Notebook(win)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>")
tab_parent.add(tab1, text=" ADMIN ")
tab_parent.add(tab2, text=" OGRETMEN ")
tab_parent.add(tab3, text=" OGRENCI ")
tab_parent.add(tab4, text=" DESTEK ")


#admin giriş
heading = Label(tab1, text = "Yönetici Girişi" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(tab1, text= "Kullanıcı Adı :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(tab1, text= "Şifre :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name1 = StringVar()
password1 = StringVar()
	
userentry1 = Entry(tab1, width=40 , textvariable = user_name1)
userentry1.focus()
userentry1.place(x=200 , y=223)

passentry1 = Entry(tab1, width=40, show="*" ,textvariable = password1)
passentry1.place(x=200 , y=260)

#öğretmen giriş
heading = Label(tab2, text = "Öğretmen Girişi" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(tab2, text= "Kullanıcı Adı :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(tab2, text= "Şifre :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name2 = StringVar()
password2 = StringVar()
	
userentry2 = Entry(tab2, width=40 , textvariable = user_name2)
userentry2.focus()
userentry2.place(x=200 , y=223)

passentry2 = Entry(tab2, width=40, show="*" ,textvariable = password2)
passentry2.place(x=200 , y=260)


#öğrenci giriş
heading = Label(tab3, text = "Öğrenci Girişi" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(tab3, text= "TC Kimlik No :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(tab3, text= "Okul No :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name3 = StringVar()
password3 = StringVar()
	
userentry3 = Entry(tab3, width=40 , textvariable = user_name3)
userentry3.focus()
userentry3.place(x=200 , y=223)

passentry3 = Entry(tab3, width=40, show="*" ,textvariable = password3)
passentry3.place(x=200 , y=260)


# giriş ve temizle butonu

btn_login1 = Button(tab1, text = "Giriş" ,font='Verdana 10 bold', command = login1)
btn_login1.place(x=200, y=293)

btn_login1 = Button(tab1, text = "Temizle" ,font='Verdana 10 bold', command = clear1)
btn_login1.place(x=260, y=293)


btn_login2 = Button(tab2, text = "Giriş" ,font='Verdana 10 bold', command = login2)
btn_login2.place(x=200, y=293)

btn_login2 = Button(tab2, text = "Temizle" ,font='Verdana 10 bold', command = clear2)
btn_login2.place(x=260, y=293)


btn_login3 = Button(tab3, text = "Giriş" ,font='Verdana 10 bold', command = login3)
btn_login3.place(x=200, y=293)

btn_login3 = Button(tab3, text = "Temizle" ,font='Verdana 10 bold', command = clear3)
btn_login3.place(x=260, y=293)












tab_parent.pack(expand=1, fill='both')
win.mainloop()
