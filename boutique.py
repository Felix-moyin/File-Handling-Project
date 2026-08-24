import sqlite3

connection = sqlite3.connect("Boutique.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        productID TEXT PRIMARY KEY,
        productName TEXT NOT NULL,
        UnitPrice INTEGER,
        AvailableQ INTEGER
    )
""")

Prods = [
    ("P101", "Men T-Shirt", 4500, 20),
    ("P102", "Womens suit dress", 90500, 30),
    ("P103", "Kids Socks", 500, 10),
    ("P104", "Unisex Loafers", 5000, 5),
    ("P105", "Anti_blu ray glasses", 4500, 20)
]

cursor.executemany("""
    INSERT OR IGNORE INTO products
    VALUES(?, ?, ?, ?)
    """, Prods)

connection.commit()

cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customerID TEXT PRIMARY KEY,
        customerName TEXT NOT NULL,
        customerEmail TEXT UNIQUE,
        phoneNo TEXT UNIQUE,
        productBought TEXT,
        quantityBought INTEGER,
        
        FOREIGN KEY(productBought) REFERENCES products(productID)
    )
""")

# cust = [
#     ("C101", "Ajibade Adesire", "09067741210", "P104", 2),
#     ("C102", "Bankola Karis", "09067541210", "P103", 5),
#     ("C103", "Alimi Iye", "09064541210", "P102", 2),
#     ("C104", "Felix Olamide", "09067741222", "P103", 2),
# ]

# cursor.executemany("""
#     INSERT OR IGNORE INTO Customers(customerID, customerName, PhoneNo, productBought, quantityBought)
#     VALUES (?, ?, ?, ?, ?)
# """, cust)



# SELECTING FROM THE TWO TABLES

# cursor.execute("""
#     SELECT customers.customerName, customers.phoneNo, customers.productBought, products.productName, products.unitPrice, customers.quantityBought 
#     FROM customers INNER JOIN products
#     ON products.productID = customers.productBought 
# """)

# for i in cursor.fetchall():
#     print()
#     print(i)




# MODIFYING TABLE STRUCTURE WITH "ALTER TABLE"

# Some common uses includes 

# cursor.execute("""
#     ALTER  TABLE products
#     RENAME COLUMN AvailableQ TO AvailableQuantity
# """)


# cursor.execute("ALTER TABLE customers DROP COLUMN customerAge")
# cursor.execute("ALTER TABLE customers ADD COLUMN customerAge INTEGER")





# UPDATE TABLE: Changes the DATA/information stored inside the table
# cursor.execute("""
#     UPDATE products
#     SET unitPrice = 1000
#     WHERE productID = "P103"
# """)

# cursor.execute("""
# UPDATE products
# SET productName = "Womens Ball Gown",
# UnitPrice = 70000
# WHERE productID = "P102"
# """)

# Update_record = [
#     (12, "C101"),
#     (20, "C102"),
#     (15, "C103"),
#     (19, "C104")
# ]

# cursor.executemany("""
#     UPDATE customers
#     SET customerAge = ?
#     WHERE customerID = ?
# """, Update_record)


# update_mail = [
#     ("dev@gmail.com", "C101"),
#     ("kariss@gmail.com", "C102"),
#     ("alimi2@gmail.com", "C103"),
#     ("felix.py@gmail.com", "C104")
# ]

# cursor.executemany("""
#     UPDATE customers
#     SET customerEmail = ?
#     WHERE customerID = ?
# """, update_mail)

# DELETE (used to delete a record)
# cursor.execute("""
#     DELETE FROM customers
#     WHERE customerID = "C101"
# """)

# DROP (used to drop the entire table)
# cursor.execute("DROP TABLE customers")

# cursor.execute("""
#     ALTER TABLE customers
#     ADD COLUMN TotalPrice INTEGER
# """)



# cursor.execute("""
#     UPDATE customers
#     SET TotalPrice = (
#         SELECT products.UnitPrice * customers.quantityBought
#         FROM products 
#         WHERE products.productID = customers.productBought
#     )
# """)

cursor.execute("""
    SELECT customers.customerName,
    customers.phoneNo,
    customers.productBought,
    products.productName,
    products.UnitPrice,
    customers.quantityBought,
    customers.TotalPrice
    FROM customers
    INNER JOIN products
    ON products.productID = customers.productBought
""")

for i in cursor.fetchall():
    name, PhoneNo, Pb, Pn, Unitp, qb, tp = i
    print(f"Name: {name} ")
    print(f"Phone Number: {PhoneNo} ")
    print(f"Product Name: {Pn} ")
    print(f"Unit Price: {Unitp} ")
    print(f"Quantity Bought: {qb} ")
    print(f"Total Price: {tp} ")
    print()
    
    





connection.commit()

print("Connection Successful ")
