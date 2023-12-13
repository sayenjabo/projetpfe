import face_recognition
import numpy as np
import os
import pickle
import DataBase as db
import cv2


class Executer:
    def __init__(self):
        
        #enregistrer les noms des patient et leur cle primer dans une liste
        print("==> names loading")
        self.faces_names = {}
        f = open("all_names.txt", "r")
        for txt in f:
            txtsplit = txt.split()
            self.faces_names[txtsplit[0]] = txtsplit[1] +" "+ txtsplit[2]
        f.close()
        print("==> names loaded")
        print (self.faces_names);
        
        #enregister les images qui sont deja encoder dans une discionaire
        #la liste faces_primekey et l'array faces_encodings utilise pour trouver le nom de chaque images avec methode zip
        self.all_face_encoding ={}
        self.faces_primekey =[]
        self.faces_encodings = np.array([])
        if os.path.getsize("all_image_incoded.dat") > 0:
            with open('all_image_incoded.dat', 'rb') as f:
                self.all_face_encoding = pickle.load(f)
            # Grab the list of faces_primekey and the list of encodings
            self.faces_primekey = list(self.all_face_encoding.keys())
            self.faces_encodings = np.array(list(self.all_face_encoding.values()))
        else:
            print("the file is empty")
        self.dbb = db.mydatabase()

    
    def found(self):
        self.takepic()
        patientface= face_recognition.load_image_file("e_image.png")
        patientface_encoded = face_recognition.face_encodings(patientface)[0] #encoder le visage

        if (len(self.faces_encodings) != 0):
             matches = face_recognition.compare_faces(self.faces_encodings, patientface_encoded) #faire une liste des caparer sur les visage deja enregistrer
             print(matches)
             
             result = set(zip(self.faces_primekey,matches))
             print(result)
             for combo in result:
                if combo[1] == True:
                    return combo[0]
                    print("the name of the patient is ",self.faces_names.get(combo[0]))
        else:
            print ("sorry there is no patient registered")
    
    def add(self,patientface,patientFirstName,patientLastName):
        
        if os.path.getsize("all_names.txt") > 0:
            print("==> calculate the nember of patiant")
            with open("all_names.txt", 'r') as fp:
                for nbr in fp:
                    pass
                print("==> the actual nbr is ",nbr)
                nbr = int(nbr[0]) + 1 #pour incrementer le conteur des cle primer de chaque patient
        else:
            nbr = 0
        
        #detecter l'emplacement des visage
        #s'il n' y a pas des visages en va arreter
        rgb_patientface = patientface[:, :, ::-1] #change the image to rgb
        patientface_location = face_recognition.face_locations(rgb_patientface) #found the face location (x,y,h,w)
        print("==> end face recherche")
        
        if (len(patientface_location) != 0):
            print("==> saving all image information")
            self.all_face_encoding[str(nbr)] = face_recognition.face_encodings(patientface)[0]
            self.faces_primekey.append(str(nbr))
            np.append(self.faces_encodings,np.array(list[face_recognition.face_encodings(patientface)[0]]))
        
            f =open("all_names.txt","a")
            if os.path.getsize("all_names.txt") > 0:
                f.write("\n"+str(nbr) +" "+patientFirstName+" "+patientLastName)
                self.faces_names[nbr] = patientFirstName +" "+ patientLastName
            else:
                f.write("0 " + patientFirstName + " " + patientLastName)
            f.close()
        
            with open('all_image_incoded.dat', 'wb') as f:
                pickle.dump(self.all_face_encoding, f)
            print("==> all faces saved with sucess")
            return True
        else:
            print("==> no face detected")
            return False
            
    def takepic(self):
        cam = cv2.VideoCapture(0)
        result, image = cam.read()
        if (result):
            # show the image
            cv2.imshow("the user face", image)
            cv2.imwrite('e_image.png', cv2.resize(image, None, fx= 0.4, fy= 0.4, interpolation= cv2.INTER_LINEAR))
        else:
            print("there is a probleme in your camera")
            return None
    
    def delete(self,id):
        with open("all_names.txt",'r') as fp:
            linesnames = fp.readlines()
            
        with open("all_names.txt",'w') as fname:
            for line in linesnames:
                self.dbb.delete(id)
                if line[0] != str(id):
                    print ("==> the id will be deleted ", line[0],"/",str(id))
                    fname.write(line)
                else:
                    try:
                        self.all_face_encoding.pop(line[0])
                        self.faces_names.pop(line[0])
                        with open('all_image_incoded.dat', 'wb') as f:
                            pickle.dump(self.all_face_encoding, f)
                    except NameError as e:
                        print(e) 
                    print('deleted from the local file')
                    
        


#img2= face_recognition.load_image_file("e_image.png")

# print("=> adding new patiant")
# Executer().add(img2,"konte", "skander")
#print("=> cherching face")
#Executer().found(img2)
#print("=> cherching face")
#Executer().delete(5)

