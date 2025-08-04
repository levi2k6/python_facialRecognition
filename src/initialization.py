import mysql.connector
from mysql.connector import Error
import faiss
import numpy
import dataManager.database as database
import os

def initialize():
    if not os.path.exists("../data/faiss.index"):
        dimension = 128
        index = faiss.IndexFlatL2(dimension)
        index = faiss.IndexIDMap(index)

        faiss.write_index(index, "../data/faiss.index")
        print("faiss.index created")
    else:
        print("faiss.index already exist")






    



