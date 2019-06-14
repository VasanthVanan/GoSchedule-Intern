# Modules imported 

import mysql.connector
import json
import subprocess

# function - to select data
def selectData(cursor):
    cursor.execute('SELECT * FROM names')
    data = json.dumps(cursor.fetchall())
    return (str(data))

# function - to insert data
def insertData(connection,cursor):
    query = "INSERT INTO names(id, name, age) values(%s,%s,%s)"
    values = ("4","Gokul","52")
    cursor.execute(query,values)
    connection.commit()

# function - to update data
def updateData(connection,cursor):
    query = "UPDATE names SET age='33' WHERE id='2'"
    cursor.execute(query)
    connection.commit()

# function - to delete data
def deleteData(connection,cursor):
    query = "DELETE FROM names where id='3'"
    cursor.execute(query)
    connection.commit()

# main-function
if __name__ == '__main__':
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }

    # MySQL Connection - 3309 Port
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Displaying the Table Data
    print("Displaying Data in names TABLE")
    print(selectData(cursor))

    # Inserting a Row in the Table
    print("Inserting the record...")
    insertData(connection,cursor)
    print(selectData(cursor))

    # Updating a Row in the Table
    print("Updating second record...")
    updateData(connection,cursor)
    print(selectData(cursor))   

    # deleting a Row in the Table
    print("deleting the 3rd record...")
    deleteData(connection,cursor)
    print(selectData(cursor))  

    # dumping the database..
    print("Dumping 'knights' database to a file.. ")
    with open('file.sql','w') as output:
        c = subprocess.Popen(['mysqldump', '-u','root','-proot','knights'],
                            stdout=output, shell=True)
    

