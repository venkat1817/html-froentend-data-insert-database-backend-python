#same directory crete two files 1.app.py , 2.db.py
import mysql.connector

# Establish connection to the MySQL database
cnx = mysql.connector.connect(
    host="database-reddy.cdcacngfasur.us-east-1.rds.amazonaws.com",
    user="admin",
    password="lkjhgfdsa",
    database="application_db"
)

def create_table():
    cursor = cnx.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            message TEXT,
            gender VARCHAR(10),
            interests VARCHAR(255)
        )
    """)
    cnx.commit()

       

