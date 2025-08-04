import face_recognition
import faiss
import cv2 
import camera
import uuid
import numpy as np
from myTypes import Person, Face
from controller import PersonController 
from dataManager import faceData

image1 = "../assets/reference2.jpg"
image2 = "../assets/capture_1754057623.jpg"

def authenticate( ):
    nameInput = input("Input name: ")
    camFace = camera.cameraCapture()

    print("camFace", camFace)

    faceEncodings = face_recognition.face_encodings(camFace)[0]
    if len(faceEncodings) == 0:
        print("No encodings found.")
        return
    faceEncodings = np.expand_dims(faceEncodings.astype(np.float32), axis=0)
    faceAuth = faceData.searchFace(faceEncodings)

    print("face_id: ", faceAuth.id)
    print("face_distance: ", faceAuth.distance)

    if faceAuth:

        person = PersonController.getPersonById(faceAuth.id)

        if person.face_id == faceAuth.id and person.name == nameInput:
            print("face matched")
            print("face distance: ", faceAuth.distance)
            print(f"Hello {person.name}, you are successfully logged in.")
        elif person.face_id != faceAuth.id:
            print(f"{person.face_id} is not equal to {faceAuth.id}")
        elif person.name != nameInput:
            print(f"{person.name} is not equal to {nameInput}")
        else:
            print("face does not match")

    else:
        print("person not found")
        return

def register():

    nameInput = input("Enter name: ")
    camFace = camera.cameraCapture()

    print("camFace: ", camFace)

    faceEncodings = face_recognition.face_encodings(camFace)[0]
    if len(faceEncodings) == 0:
        print("No encodings found.")
        return
    faceEncodings = np.expand_dims(faceEncodings.astype(np.float32), axis=0)
    faceAuth = faceData.searchFace(faceEncodings)

    print("faceAuth: ", faceAuth)

    if faceAuth:
        if faceAuth.distance < 0.5:
            print("User already exist.")
            return
        print("User exist but face distance is wrong?")

    myUuid = str(uuid.uuid4())
    person = Person(id = myUuid, name = nameInput, face_id = None, face = None)
    PersonController.addPerson(person)
    personDb = PersonController.getPersonByName(nameInput)
    face = Face(id = personDb.face_id, data = faceEncodings)
    faceData.addFace(face)
    print("Register success")

