import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from executer import Executer as exe
import DataBase as dab
import face_recognition


root = tk.Tk()
root.title('formulaire')
root.geometry('800x500')
playFrame = tk.Frame(root)
executer = exe()
database= dab.mydatabase()

        

prenom = tk.Label(root, text="Prenom:")
nom = tk.Label(root, text="Nom: ") 
tel = tk.Label (root, text="Telephone:")
date_naissance= tk.Label(root, text="Date de naissance:")
date_RDV= tk.Label(root, text="Date de RDV:")
description= tk.Label(root, text="Description: ")
image= tk.Label(root, text="image: ")

e_prenom = tk.Entry(root, width=35)
e_nom = tk.Entry(root, width=35)
e_tel = tk.Entry(root, width=35)
e_date_naissance = tk.Entry(root, width=35)
e_date_RDV = tk.Entry(root, width=35)

try:
    e_image = tk.PhotoImage(file ="press_here.png")
except NameError as e:
    print(e)
b_image = tk.Button(root, image=e_image)

def changepic(event):
    try:
        print(event.widget.cget('image'))
        executer.takepic()    
        e_image = tk.PhotoImage(file ="e_image.png")
        b_image.configure(image = e_image)
        b_image.photo = e_image
        print("updated")
    except NameError as e:
        print(e)
        
        
def ajouter():
    if ( (len(e_nom.get())>0) & (len(e_prenom.get())>0) & (len(e_tel.get())>0) & (len(e_date_naissance.get())>0) & (len(e_date_RDV.get())>0) ):
        if(executer.add(face_recognition.load_image_file("e_image.png"), e_prenom.get(), e_nom.get())):
            database.ajou(e_nom.get(), e_prenom.get(), e_tel.get(), e_date_naissance.get(), e_date_RDV.get(),[e_date_RDV.get()])
        else:
            print("please put another face")
    else:
        print("please make sure to put every thing")
    
    
b_image.bind('<Button-1>', changepic)

nom.grid(row=0, column=3, padx=15, pady=10)
e_nom.grid(row=0,column=4, padx=15)

prenom.grid(row=1, column=3, padx=15, pady=10)
e_prenom.grid(row=1,column=4, padx=15)

tel.grid(row=2, column=3, padx=15, pady=10)
e_tel.grid(row=2,column=4, padx=15)

date_naissance.grid(row=3, column=3, padx=15, pady=10)
e_date_naissance.grid(row=3,column=4, padx=15)

date_RDV.grid(row=4, column=3, padx=15, pady=10)
e_date_RDV.grid(row=4,column=4, padx=15)


image.grid(row=1, column=0, padx=15, pady=10)
b_image.grid(row=1,column=1, padx=15)


enregistre= tk.Button(root, text="Enregistre",command = ajouter, width="20")
enregistre.grid(row=10, column=2, columnspan=2, padx=20, pady=40)


root.mainloop()
