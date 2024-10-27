import mysql.connector
from mysql.connector import Error

def create_database():
    database_name = "alx_book_store"
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor._execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
            print(f"Database '{database_name}' created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            
if __name__ == "__main__":
    create_database()