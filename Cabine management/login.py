from tkinter import *
import os

global dct
dct = {}
def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("cabinets Medicales")
  screen3.geometry("400x400")
    
  def importer():
    
    f = open('contacts.txt','r')
    
    for ch in f:
        l = ch.split(':')
        nom = l[0]
        ln = l[1].split('|')
        #ln[-1] = ln[-1][:len(ln[-1])-1]
        dct.update({nom:ln[:len(ln)-1]})
    f.close()

  def ajouter (dct):
    
    nom=(input("tapez votre nom \n"))
    prenom=input("tapez votre prenom \n")
    tel=input("tapez le numero de tel\n ")
    sante=input("rediger le cas de cette maladie\n")
    dct.update({nom+prenom+sante:[tel]})
    
  def rendezvous(liste):
    app.withdraw()
    nom=input("nom du  reservateur\n ");
    temps=input("temps de reservation avec jj/mm/aa :\n");
    tel=input("tapez telephone\n ");
    while temps  in liste :
        temps=input("impossibe de reserver dans ce temps merci de rechoisir\n")
    app.deiconify()    
    
  def supp(dct):
    
    
    nom=(input("tapez votre nom \n"))
    prenom=input("tapez votre prenom \n")
    if nom+prenom in dct:
        dct.pop(nom+prenom)
    else:
        print("nom nexsite pas")
    
    
  def update(dct):
    
    nom=(input("tapez votre nom \n"))
    prenom=input("tapez votre prenom \n")
    tel=input("tapez votre numero\n")
    if nom+prenom not in dct:
        dct.update({nom+prenom:[tel]})
    else:
        dct[nom+prenom].append(tel)

    

  def recherche_num(dct):
    
    nom=(input("tapez votre nom \n"))
    prenom=input("tapez votre prenom \n")
    if nom+prenom in dct:
        print (dct[nom+prenom])
    else:
        print("\n nom existe pas\n")
    
  def exporter(d):
    f = open('contacts.txt','w+')
    f.seek(0)
    f.truncate()
    for key in d:
        ch=''
        ch = key+':'
        for i in d[key]:
            ch += i + '|'
        ch = ch+'\n'
        f.write(ch)       

        


  Button(screen3, text = "Ajouter  fiche",height = "2", width = "30", command =lambda: ajouter(dct)).pack()
  Button(screen3, text = "Creer rendez vous",height = "2", width = "30", command =lambda: supp(dct)).pack()
  Button(screen3, text = "Modifier fiche",height = "2", width = "30", command =lambda: update(dct)).pack()
  Button(screen3, text = "Rech_num client",height = "2", width = "30", command =lambda: lambda: recherche_num(dct)).pack()
  Button(screen3, text = "Supprimer fiche",height = "2", width = "30", command =lambda: supp(dct)).pack()
  Button(screen3, text = "Exporter",height = "2", width = "30", command =lambda: exporter(dct)).pack()
  Button(screen3, text = "Importer",height = "2", width = "30", command =lambda: importer()).pack()


  Button(screen3, text = "Afficher",height = "2", width = "30", command =lambda:print(dct)).pack()
  Button(screen3, text = "Quitter",height = "2", width = "30", command =lambda:app.destroy()).pack()

  
  
  









  

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Notes 1.0")
  Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
