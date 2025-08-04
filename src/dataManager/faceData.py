import faiss
import numpy as np
from dotenv import load_dotenv
import os

from myTypes import FaceAuth, Face 


index = faiss.read_index( os.getenv("faceDataLocation") )

def addFace( face: Face ):

    print("face data: ", face.data)
    print("face id: ", face.id, np.array([face.id], dtype=np.int64))

    try:
        index.add_with_ids(face.data, np.array([face.id], dtype=np.int64))
        print("Face added succesfully.")
        faiss.write_index(index, os.getenv("faceDataLocation"))
    except Exception as error:
        print("Faiss error: ", error)


def searchFace(face):

    distance, id = index.search(face, k=1)

    if id[0][0] == -1:
        print("No match found")
        return False 
    else:
        print(f"Match found: face_id = {id[0][0]}, distance = {distance[0][0]}")
        return FaceAuth(id=int(id[0][0]), distance=float(distance[0][0]))  
