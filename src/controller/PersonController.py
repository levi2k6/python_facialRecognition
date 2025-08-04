from mysql.connector import Error
import dataManager.database as database
from myTypes import Person
import numpy as np

def addPerson( person: Person ):
    try:
        database.cursor.execute("INSERT INTO person(id, name) VALUES (%s, %s)", (person.id, person.name))
        database.connection.commit()
        print("Successfully added a person")
    except Error as error:
        print("Error while executing query: ", error)

def getAllPerson():
    try:
        database.cursor.execute("SELECT * FROM person" )
        row = database.cursor.fetchone()
        if row is None:
            return
        print("row: ", row)
    except Error as error:
        print("Error while executing query: ", error)
    
def getPersonByName(name):
    try:
        database.cursor.execute("SELECT * FROM person WHERE name = (%s)", (name,)) 
        row = database.cursor.fetchone()

        if row is None:
            return None

        return Person(
            id = row["id"],
            name = row["name"],
            face_id = row["face_id"],   
            face = None
        )
    except Error as error:
        print("Error while executing query: ", error)
        return False


def getPersonById(id):
    try:
        database.cursor.execute("SELECT * FROM person WHERE face_id = (%s)", (id,)) 
        row = database.cursor.fetchone()

        if row is None:
            return None

        return Person(
            id = row["id"],
            name = row["name"],
            face_id = row["face_id"],   
            face = None
        )
    except Error as error:
        print("Error while executing query: ", error)
        return False


 