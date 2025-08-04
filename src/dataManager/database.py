from dotenv import load_dotenv 
import os
import mysql.connector
from mysql.connector import Error
import numpy as np

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../", ".env"))
print("host:", os.getenv("host"))
print("user:", os.getenv("user"))
print("password:", os.getenv("password"))
print("database:", os.getenv("database"))
connection = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)

cursor = connection.cursor(dictionary=True)





