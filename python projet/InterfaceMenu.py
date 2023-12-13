import customtkinter as ctk 
import os
import subprocess

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
Menu = ctk.CTk()
Menu.geometry("500x350")

def connexion(file_path):
    try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         print("Execution successful.")
         print("Output:")
         print(completed_process.stdout)
      else:
         print(f"Error: Failed to execute '{file_path}'.")
         print("Error output:")
         print(completed_process.stderr)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

    print("Bienvenue")

frame  = ctk.CTkFrame(master=Menu, bg_color="white", fg_color="#D6E8FE")
frame.pack(pady = 20, padx=80, fil = "both", expand=True )

label = ctk.CTkLabel(master = frame, text="Bien Venu", text_color="red", font=("Arial", 20))
label.pack(pady = 12, padx=10)

button1 = ctk.CTkButton(master = frame, text="Ajouter un patient", command=lambda:connexion("FormulairePatient.py"), width=160, height=30, fg_color="#1E7FCB",font=("Helvetica", 15))
button1.pack(pady = 20, padx=10)

button2 = ctk.CTkButton(master = frame, text="liste de patients", width=160, height=30 ,command=lambda:connexion("liste.py"),fg_color="#1E7FCB", font=("Helvetica", 15))
button2.pack(pady = 20, padx=10)

button3 = ctk.CTkButton(master = frame, text="Recherche d'un patient",width=100, height=30, command= lambda:connexion("Rechercher.py"),fg_color="#1E7FCB", font=("Helvetica", 15))
button3.pack(pady = 20, padx=10)
Menu.mainloop()
