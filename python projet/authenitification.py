import customtkinter as ctk 
import subprocess

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
login = ctk.CTk()
login.geometry("500x350")


def connexion(file_path):
    completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
    login.destroy()
    if completed_process.returncode == 0:
       print("Execution successful.")
       print("Output:")
       print(completed_process.stdout)


 
frame  = ctk.CTkFrame(master=login)
frame.pack(pady = 20, padx=60, fil = "both", expand=True )

label = ctk.CTkLabel(master = frame, text="se connecter")
label.pack(pady = 12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Identifiant")
champ1.pack(pady = 12)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
champ2.pack(pady = 12)
button = ctk.CTkButton(master = frame, text="connexion", command=lambda :connexion("InterfaceMenu.py"))
button.pack(pady = 12, padx=10)

login.mainloop()