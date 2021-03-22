import mysql.connector as mysql


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "?",
    database = "testPython_DB"
)

# Print db Object to confirm connection to db
# print(db)


# Creating an instance of cursor class which is used to execute the SQL statements in Python
cursor = db.cursor()

# Create database 
# Execute method is used to compile an SQL statement
# cursor.execute("CREATE DATABASE testPython_DB")

# Show the current dbs
cursor.execute("SHOW DATABASES")

# Fetchall() method fetches all the rows from the last executed statement
databases = cursor.fetchall() # Returns a list of all present dbs
#print(databases)


cursor.execute("SHOW TABLES")
tables = cursor.fetchall() # Returns a list of all present tables in the db

# Creating tables
# First select the database in the SQL connect statement

#cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

for table in tables:
    print(table)

# Drop table to create again with primary key
#cursor.execute("DROP TABLE users")

# Create table again with PK
#cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), username VARCHAR(255))")

# DESC used to get all columns information
#cursor.execute("DESC users")
#print(cursor.fetchall())

# Drop PK
#cursor.execute("ALTER TABLE users DROP id")
#cursor.execute("DESC users")
#print(cursor.fetchall())


# Adding PK
# First keyword will add column to first column in table

#cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
#cursor.execute("DESC users")
#print(cursor.fetchall())

# Inserting Data

# Inserting single row
# Defining the query
#values = ('Tobias', 'toby')
#query = "INSERT INTO users (name, username) VALUES (%s, %s)"


# Executing the query with the values
#cursor.execute(query)
# To make final we run commit method on db object
#db.commit()
#print(cursor.rowcount, "record inserted")


# Inserting multiple rows
"""
query = "INSERT INTO users (name, username) VALUES (%s,%s)"
values = [
    
    ("Peter", "peter"),
    ("Sarah", "sarah"),
    ("Tomas", "tomas"),
    ("Hannah", "hannah")
]
cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "records inserted")
"""

# Select Data
# Getting all records from table

query = "SELECT * FROM users"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)

# Getting some columns

query = "SELECT username, name FROM users"
cursor.execute(query)
usernames = cursor.fetchall()
for user in usernames:
    print(user)

# Where is used to select data on some condition
query = "SELECT * FROM users WHERE name = 'hannah' ORDER BY id DESC"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)

# DELETE from table
#query = "DELETE FROM users WHERE id = 5"
#cursor.execute(query)
#db.commit()
#records = cursor.fetchall()
#for record in records:
    #print(record)


# UPDATE records in table
query = "UPDATE users SET name = 'Jessica' WHERE name = 'Sarah'"
cursor.execute(query)
db.commit()
query = "SELECT * FROM users"
records = cursor.fetchall()
for record in records:
    print(record)