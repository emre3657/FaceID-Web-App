import os
import mysql.connector # type: ignore
from dotenv import load_dotenv

load_dotenv()

def connectDatabase():
    # MySQL bağlantısı oluşturma
    mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST"), 
    port=os.environ.get("DB_PORT"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
    )
    mycursor = mydb.cursor()
    return mycursor, mydb