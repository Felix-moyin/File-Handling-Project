import sqlite3

link = sqlite3.connect("Restaurant.db")
cursor = link.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers(
        CustomerId INTEGER PRIMARY KEY AUTOINCREMENT,
        Most_ordered_food TEXT,
        Customer_location TEXT,
        Age INTEGER,
        Phone_Number INTEGER UNIQUE
    )
""")


customer = [
    ('Jollof Rice', 'Akobo, Ibadan', 30, +2347015300929),
    ('Spaghetti', 'Taska, Ibadan', 21, +2347012300929),
    ('Fried Rice', 'Ring-Road, Ibadan', 25, +2349039350929),
    ('Jollof Rice', 'Alakia, Ibadan', 30, +2347070300929),
    ('Salad', 'Akobo, Ibadan', 20, +2347080300929),
    ('Poundo with vegetables', 'Gate, Ibadan', 23, +2347045300929),
    ('Fruits', 'Iyana Church, Ibadan', 29, +2340815300929),
]

cursor.executemany("""
    INSERT  OR IGNORE INTO Customers( Most_ordered_food, Customer_location, Age, Phone_Number)
    VALUES(?, ?, ?, ?)     
""", customer)

#  #Question mark is a place holder
link.commit()

# print(cursor.fetchall())
# cursor.execute("SELECT Phone_Number FROM customers")
# for i in cursor.fetchall():
#     print(i)


print("Link Successfully")




# Foreign key is a field or attribute in one table that uniquely points to a primary key in another table.  
