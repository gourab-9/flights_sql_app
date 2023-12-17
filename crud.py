import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '123456',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print('Connection Established')
except:
    print('Connection Error')


# Create a database on the db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# Create Table
# airport -> airport_id | code | name
#mycursor.execute("""
#CREATE TABLE airport(
#        airport_id INTEGER PRIMARY KEY,
#        code VARCHAR (10) NOT NULL,
#        city VARCHAR (50) NOT NULL,
#        name VARCHAR (255) NOT NULL
#)
#""")
#conn.commit()

# Insert data to the table
# mycursor.execute("""
#        INSERT INTO airport VALUES
#        (1,'DEL','New Delhi','IGIA'),
#        (2,'CCU','Kolkata','NSCA'),
#        (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()


# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id >= 1 ")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])


# UPDATE

mycursor.execute("""
UPDATE airport
SET city = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1 ")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3 ")
conn.commit()

# Search/Retrieve
mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)