import firebase_admin
from firebase_admin import credentials,db,storage
import os

class mydatabase():
    
   
    def __init__(self):
        if not firebase_admin._apps:
            self.cred_obj = firebase_admin.credentials.Certificate("projet-python-6bdcd-firebase-adminsdk-o0hme-3a078f1a11.json")
            self.default_app = firebase_admin.initialize_app(self.cred_obj,{
                                                                            'databaseURL':'https://projet-python-6bdcd-default-rtdb.firebaseio.com/',
                                                                            'storageBucket' :'https://projet-python-6bdcd-default-rtdb.firebaseio.com/'
                                                                            })
           
        
    def ajou(self,nom,prenom,tel,dateDeNaissance,date_RDV1,liste):           
        with open("all_names.txt", 'r') as fp:
            for nbr in fp:
                pass
            nbr = int(nbr[0])
            print('==> Total Number of lines:', nbr)
            

        #bucket = storage.bucket()
        #blob = bucket.blob('2.jpg')
        #blob.download_to_filename(r'C:\Users\konte\Desktop\Cabinet\projet\2.jpg')
        
        #storage = pyrebase.initialize_app(self.Config).storage()
        #blob.upload_from_filename('all_image_incoded.dat')       
        
        
        ref = db.reference("/")
        primerykey ="patient "+str(nbr) 
        ref.child(primerykey).set({
        
         	  "id": nbr, 
		      "Nom": nom,
              "Prenom":prenom,
              "Tel":tel,
              "Date_naissance":dateDeNaissance,
              "Date_RDV1":date_RDV1,
              "Description":"",
              "liste":liste
 	    	
        })
        print ("==> added to the database with sucess")
        
    def loadfile(self):
        ref = db.reference("/")
        data = ref.get()
        #(data)
        with open("all_names.txt", "w") as f:
            for value in data.values():
                if os.path.getsize("all_names.txt") > 0: 
                    f.write("\n"+str(value.get("id")) +" "+value.get("Nom")+" "+value.get("Prenom"))
                else:
                    f.write(str(value.get("id")) +" "+value.get("Nom")+" "+value.get("Prenom"))
        print("==> load with succes")
        
        
    def delete(self,id):
        ref = db.reference("/")
        data = ref.get()
        for info in data.keys():
            if ( info =="patient "+str(id)):
                print(info)
                db.reference("/"+info).delete()
                print("deleted from the database")
                
    def sendData(self,patientkey,description):
        ref = db.reference("/")
        ref.child(patientkey+"/Description").set(description)
        
    def get(self,idkey):
        ref = db.reference("/")
        if idkey != "all" :
            return ref.child(idkey).get()
        else:
            return ref.get()
        
            
        
        
#mydatabase().ajou("konte","skadner","92789406","2/6/2020","12/12/2025",["12/12/2026"])
#mydatabase().loadfile()
#mydatabase().delete(2)