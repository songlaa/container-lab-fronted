from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def get_users():
    # Fetch environment variables
    servername = os.getenv('servername')
    username = os.getenv('username')
    password = os.getenv('password')

    # Connect to MariaDB
    try:
        connection = mysql.connector.connect(
            host=servername,
            user=username,
            password=password,
            database='mysql',
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT User FROM mysql.user")
        users = cursor.fetchall()
        
        # Create an HTML response
        result = "<h1>Users:</h1><ul>"
        for user in users:
            result += f"<li>{user[0]}</li>"
        result += "</ul>"

        cursor.close()
        connection.close()
        return result

    except mysql.connector.Error as err:
        return f"Error: {err}"
