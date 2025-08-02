import mysql.connector
import numpy as np
from typing import Optional
from myTypes import Person 

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="levi123",
    database="facedb"
)

cursor = connection.cursor(dictionary=True)

def addPerson( person: Person ):
    face = person.face.astype(np.float32).tobytes() 
    cursor.execute("INSERT INTO person(name, face) VALUES (%s, %s)", (person.name, face))
    connection.commit()

def getPerson(name):
    cursor.execute("SELECT * FROM person WHERE name = (%s)", (name,)) 
    row = cursor.fetchone()

    if row is None:
        return None

    return Person(
        name = row["name"],
        face = np.frombuffer(row["face"], dtype=np.float32)  
    )


