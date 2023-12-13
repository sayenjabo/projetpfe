import sqlite3
from tkinter import *
from tkinter import ttk
from executer import Executer
import DataBase

root = Tk()
root.title("Inventory System")
root.geometry("1100x500")
my_tree = ttk.Treeview(root)
exe = Executer()
db = DataBase.mydatabase()


def refresh():
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    contacts = []
    db.loadfile()
    patients = db.get("all")
    for idkey in patients.keys():
        tel = patients.get(idkey).get("Tel")
        name = patients.get(idkey).get("Nom")
        prenom = patients.get(idkey).get("Prenom")
        contacts.append((idkey, name, prenom, tel ,patients.get(idkey).get("id")))
    
    for result in contacts:
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
    


def delete(data):
    exe.delete(data)


def update(identif = "", nom = "", Prenom = "", telephone= ""):
    contacts = []
    db.loadfile()
    patients = db.get("all")
    for idkey in patients.keys():
        print(idkey)
        id = patients.get(idkey).get("id")
        tel = patients.get(idkey).get("Tel")
        name = patients.get(idkey).get("Nom")
        prenom = patients.get(idkey).get("Prenom")
        
        tel_result =  (True) if (telephone == "") else (tel == telephone)
        print(tel_result)
        name_result =  (True) if (nom == "") else (name == nom)
        print(name_result)
        prenom_result =  (True) if (Prenom == "") else (Prenom == prenom)
        print(prenom_result)
        id_result =  (True) if (identif == "") else (id == int(identif))
        print (prenom_result)
        if ((prenom_result) & (tel_result) & (name_result) & (id_result)):
            contacts.append((idkey, name, prenom, tel ,id))
    
    for result in contacts:
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")


def delete_data():
    selected_item = my_tree.focus()
    print(selected_item)
    deleteData = my_tree.item(selected_item).get('values')[-1]
    print("the data is ",deleteData)
    delete(deleteData)
    print("done")
    refresh()

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    for data in my_tree.get_children():
        my_tree.delete(data)

    print(e_Id.get())
    update(e_Id.get(), e_Name.get(), e_Prenom.get(), e_Telephone.get())
    


def Description():
    selected_item = my_tree.focus()
    patientkey = my_tree.item(selected_item).get('values')[0]
    patients = db.get("all")
    descrip = patients.get(patientkey).get("Description")
    
    global newWindow
    root.withdraw()
    newWindow = Toplevel()
    newWindow.geometry("600x300")
    Description = Text(newWindow)
    Description.insert(INSERT,descrip)
    Description.configure(width=50 ,height=40)
    Description.grid(row=1, column=0, columnspan=1)
    
    b_menu = Button(newWindow, text = "save",command =lambda :show(patientkey,Description.get('1.0',END)))
    b_menu.grid(row=0, column=0, columnspan=1)

def show(patientkey,Description):
    db.sendData(patientkey, Description)
    root.update()
    root.deiconify()
    newWindow.destroy()
    
def fetch():
    patientid = exe.found()
    
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    print(patientid)
    update(identif = patientid)
    
#########################title##############################
titleLabel = Label(root, text="recherche patient", font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=1, columnspan=8, padx=20, pady=20)

#############################title left#######################################
idLabel = Label(root, text="ID", font=('Arial bold', 15))
NameLabel = Label(root, text="Name", font=('Arial bold', 15))
PrenomLabel = Label(root, text="Prenom", font=('Arial bold', 15))
TelephoneLabel = Label(root, text="Telephone", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
NameLabel.grid(row=2, column=0, padx=10, pady=10)
PrenomLabel.grid(row=3, column=0, padx=10, pady=10)
TelephoneLabel.grid(row=4, column=0, padx=10, pady=10)

#############################zone de text################################
e_Id = Entry(root, width=25, bd=5, font=('Arial bold', 15))
e_Name = Entry(root, width=25, bd=5, font=('Arial bold', 15))
e_Prenom = Entry(root, width=25, bd=5, font=('Arial bold', 15))
e_Telephone = Entry(root, width=25, bd=5, font=('Arial bold', 15))
e_Id.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
e_Name.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
e_Prenom.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
e_Telephone.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

#############################bouton###########################################
b_Refresh = Button(root, text="refresh", padx=5, pady=5, width=5,bd=3, font=('Arial', 15), bg="#0099ff", command=refresh)
b_Refresh.grid(row=5, column=1, columnspan=1)
b_research = Button(root, text="research", padx=5, pady=5, width=6,bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
b_research.grid(row=5, column=2, columnspan=1)
b_Delete = Button(root, text="Delete", padx=5, pady=5, width=5,bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
b_Delete.grid(row=5, column=3, columnspan=1)
b_menu = Button(root, text="Description", padx=5, pady=5, width=7,bd=3, font=('Arial', 15), bg="#e62e00" , command = Description)
b_menu.grid(row=6, column=2, columnspan=1)
b_face = Button(root, text="facerecog", padx=5, pady=5, width=7,bd=3, font=('Arial', 15), bg="#e62e00" , command = fetch)
b_face.grid(row=6, column=1, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

##############################affichage#################################
my_tree['columns'] = ("ID", "Nom", "Prenom", "Telephone")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Nom", anchor=W, width=200)
my_tree.column("Prenom", anchor=W, width=150)
my_tree.column("Telephone", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Nom", text="Name", anchor=W)
my_tree.heading("Prenom", text="Prenom", anchor=W)
my_tree.heading("Telephone", text="Telephone", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()

