import sqlite3

# dbms --> database --> tables --> data

connection = sqlite3.connect("School.db")
# connect() is use to create database or connect an existing database
cursor = connection.cursor()



# CREATING TABLE
# You definethe schema (structure) of a table using the command CREATE TABLE.
# The attributes come in, followed  by the datatype and lastly the constraints

# DATATYPES:
# INTEGERS : Whole number e.g (age: 45, 18)
# REAL : Decimal numbers e.g (Weight: 50.9 or GPA: 4.78)
# TEXT: Strings e.g (name: "Olamide")
# NULL: Represents no value/unknown


# CONSTRAINTS
# PRIMARY KEY - The column should uniquely identifies each now
# AUTO INCREMENT -SQLite should automatically generates the next id for you,so you never have to track it yourself. e.g 1, 2, 3, 4...
# NOT NULL - this column can not b empty
# UNIQUE - No two rows can have the same value in this column

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        Std_id INTEGER PRIMARY KEY AUTOINCREMENT,
        First_name TEXT NOT NULL,
        Last_name TEXT NOT NULL,
        Age INTEGER,
        Department TEXT,
        Email TEXT UNIQUE
    )
""")

# Research and insert data into the tables we just created
# Create a new database - Resturant, Table - Customer with attribute customer_id, most_ordered_food, customer_location and  age and email or phone
# Insert data into the customer table

# What is a Foreign key

students = [
    ("Felix", "Moyinoluwa", 18, "Data Analysis", "felix@email.com"),
    ("John", "Adeola", 27, "Cyber Security", "john@email.com"),
    ("Mary", "Ajayi", 21, "Data Science", "mary@email.com"),
    ("David", "Okafor", 23, "Data Science", "david@email.com"),
    ("Sarah", "Bello", 20, "Information Technology", "sarah@email.com")
]

cursor.executemany("""
    INSERT  OR IGNORE INTO Students (First_name, Last_name, Age, Department, Email)
    VALUES (?, ?, ?, ?, ?)
""", students)

connection.commit()

# cursor.execute("SELECT First_name, Age FROM Students WHERE Age < 27")
# for i in cursor.fetchall():
#     print(i)
    
cursor.execute("SELECT * FROM Students WHERE Last_name == 'Okafor' ")
print(cursor.fetchall())

print("Connection Successful")