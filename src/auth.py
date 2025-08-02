import face_recognition
import cv2 
import camera
from myTypes import Person 

import database 

image1 = "../assets/reference2.jpg"
image2 = "../assets/capture_1754057623.jpg"

def authenticate( ):
    nameInput = input()
    camFace = camera.cameraCapture()

    print("camFace: ", camFace)

    user = database.getUser(nameInput)

    if user:
        face1_encoding = face_recognition.face_encodings(camFace)[0]

        results = face_recognition.compare_faces([face1_encoding], user.face)
        face_distance = face_recognition.face_distance([face1_encoding], user.face)

        if results[0]:
            print("face matched")
        else:
            print("face does not match")
 
        print("face distance: ", face_distance[0])
    else:
        print("user not found")
        return

def register():

    userInput = input("Enter name: ")
    camFace = camera.cameraCapture()

    face_encoding = face_recognition.face_encodings(camFace) 
    person = Person(userInput, face_encoding)

    database.addPerson(person)

