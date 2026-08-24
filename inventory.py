import sqlite3

con = sqlite3.connect("inventory.db")
cursor = con.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")


# ============================================================
# QUESTION A
# CREATING THE TWO TABLES
# ============================================================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers(
        supplierID TEXT NOT NULL PRIMARY KEY,
        supplierName TEXT NOT NULL,
        PhoneNo TEXT UNIQUE NOT NULL        
    )        
""")            # Created a table called suppliers


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inve_Products(
        productID TEXT NOT NULL PRIMARY KEY,
        productName TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        supplierID TEXT NOT NULL,

        FOREIGN KEY (supplierID) REFERENCES suppliers(SupplierID)
    )
""")           # Created a table called Inve_Products


print()
print("========== QUESTION A ==========")
print("Tables created successfully.")
print()


# ============================================================
# QUESTION B
# INSERTING AT LEAST 8 SUPPLIERS
# ============================================================

sup = [
    ("S001", "ABC Foods", "08031234567"),
    ("S002", "FreshMart Suppliers", "08042345678"),
    ("S003", "Golden Harvest", "08153456789"),
    ("S004", "Prime Distributors", "08064567890"),
    ("S005", "Daily Needs Ltd", "08175678901"),
    ("S006", "TopChoice Foods", "08086789012"),
    ("S007", "Value Plus", "08197890123"),
    ("S008", "Mega Supply", "08018901234")
]

cursor.executemany("""
    INSERT OR IGNORE INTO suppliers
    VALUES (?, ?, ?)
""", sup)

print("========== QUESTION B ==========")
print("8 suppliers inserted successfully.")
print()


# ============================================================
# QUESTION C
# INSERTING AT LEAST 15 PRODUCTS
# ============================================================

prod = [
    ("P001", "Rice", 50, "S001"),
    ("P002", "Beans", 35, "S001"),
    ("P003", "Spaghetti", 25, "S002"),
    ("P004", "Cooking Oil", 18, "S002"),
    ("P005", "Sugar", 40, "S003"),
    ("P006", "Milk", 15, "S003"),
    ("P007", "Bread", 30, "S004"),
    ("P008", "Biscuits", 45, "S004"),
    ("P009", "Tomato Paste", 22, "S005"),
    ("P010", "Corn Flakes", 12, "S005"),
    ("P011", "Detergent", 28, "S006"),
    ("P012", "Toilet Soap", 20, "S006"),
    ("P013", "Bottled Water", 60, "S007"),
    ("P014", "Soft Drink", 32, "S008"),
    ("P015", "Tea", 10, "S008")
]

cursor.executemany("""
    INSERT OR IGNORE INTO Inve_Products
    (ProductID, ProductName, Quantity, SupplierID)
    VALUES (?, ?, ?, ?)
""", prod)

print("========== QUESTION C ==========")
print("15 products inserted successfully.")
print()


# ============================================================
# QUESTION D
# DISPLAY EVERY SUPPLIER
# ============================================================

cursor.execute("""
    SELECT * FROM Suppliers
""")

print("========== QUESTION D ==========")
print()

for supplier in cursor.fetchall():

    supplier_id, supplier_name, phone = supplier

    print(f"Supplier ID: {supplier_id}")
    print(f"Supplier Name: {supplier_name}")
    print(f"Phone Number: {phone}")
    print()


# ============================================================
# QUESTION E
# DISPLAY EVERY PRODUCT
# ============================================================

cursor.execute(""" 
    SELECT * FROM Inve_Products 
""")

print("========== QUESTION E ==========")
print()

for product in cursor.fetchall():

    product_id, product_name, quantity, supplier_id = product

    print(f"Product ID: {product_id}") 
    print(f"Product Name: {product_name}") 
    print(f"Quantity: {quantity}") 
    print(f"Supplier ID: {supplier_id}")
    print()


# ============================================================
# QUESTION F
# DISPLAY PRODUCTS WITH QUANTITY GREATER THAN 20
# ============================================================

cursor.execute(""" 
    SELECT * FROM Inve_Products
    WHERE quantity > 20
""")

print("========== QUESTION F ==========")
print()

for q20 in cursor.fetchall():

    product_id, product_name, quantity, supplier_id = q20

    print(f"Product Name -> {product_name}")
    print(f"Product Id -> {product_id}")
    print(f"Product Quantity -> {quantity}")
    print()


# ============================================================
# QUESTION G
# INNER JOIN
# ============================================================

cursor.execute("""
    SELECT Inve_Products.ProductName, Suppliers.SupplierName
    FROM Inve_Products
    INNER JOIN Suppliers
    ON Inve_Products.SupplierID = Suppliers.SupplierID
""")

print("========== QUESTION G ==========")
print()

for item in cursor.fetchall():

    product_name, supplier_name = item

    print(f"{product_name} is supplied by {supplier_name}.")
    print()


# ============================================================
# QUESTION H
# ADD UNITPRICE TO PRODUCTS
# ============================================================

cursor.execute("""
    ALTER TABLE Inve_Products
    ADD COLUMN UnitPrice INTEGER
""")

print("========== QUESTION H ==========")
print("UnitPrice column added successfully.")
print()


# ============================================================
# QUESTION I
# RENAME PRODUCTNAME TO ITEMNAME
# ============================================================

cursor.execute("""
    ALTER TABLE Inve_Products
    RENAME COLUMN ProductName TO ItemName
""")

print("========== QUESTION I ==========")
print("ProductName has been renamed to ItemName.")
print()


# ============================================================
# QUESTION J
# UPDATE THE PRICES OF ALL PRODUCTS AT ONCE
# ============================================================

prices = [
    (35000, "P001"),
    (25000, "P002"),
    (5000, "P003"),
    (12000, "P004"),
    (8000, "P005"),
    (4500, "P006"),
    (2000, "P007"),
    (3500, "P008"),
    (2500, "P009"),
    (6000, "P010"),
    (5000, "P011"),
    (1500, "P012"),
    (500, "P013"),
    (1000, "P014"),
    (3000, "P015")
]

cursor.executemany("""
    UPDATE Inve_Products
    SET UnitPrice = ?
    WHERE ProductID = ?
""", prices)

print("========== QUESTION J ==========")
print("Prices updated successfully.")
print()


# Display the updated prices

cursor.execute("""
    SELECT * FROM Inve_Products
""")

for product in cursor.fetchall():

    product_id, item_name, quantity, supplier_id, unit_price = product

    print(f"Product ID: {product_id}")
    print(f"Item Name: {item_name}")
    print(f"Unit Price: ₦{unit_price}")
    print()


# ============================================================
# QUESTION K
# CALCULATE REVENUE GENERATED
# ============================================================

cursor.execute("""
    SELECT ItemName, Quantity, UnitPrice,
           Quantity * UnitPrice
    FROM Inve_Products
""")

print("========== QUESTION K ==========")
print()

for item in cursor.fetchall():

    item_name, quantity, unit_price, revenue = item

    print(f"Item Name: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ₦{unit_price}")
    print(f"Revenue: ₦{revenue}")
    print()


cursor.execute("""
    SELECT SUM(Quantity * UnitPrice)
    FROM Inve_Products
""")

total_revenue = cursor.fetchone()[0]

print(f"Total Revenue: ₦{total_revenue}")
print()


# ============================================================
# QUESTION L
# DELETE ONE PRODUCT
# ============================================================

cursor.execute("""
    DELETE FROM Inve_Products
    WHERE ProductID = 'P015'
""")

print("========== QUESTION L ==========")
print("Product P015 has been deleted.")
print()


# ============================================================
# QUESTION M
# TOTAL NUMBER OF PRODUCTS
# ============================================================

cursor.execute("""
    SELECT COUNT(*)
    FROM Inve_Products
""")

total_products = cursor.fetchone()[0]

print("========== QUESTION M ==========")
print(f"Total number of products: {total_products}")
print()


# ============================================================
# QUESTION N
# TOTAL NUMBER OF SUPPLIERS
# ============================================================

cursor.execute("""
    SELECT COUNT(*)
    FROM Suppliers
""")

total_suppliers = cursor.fetchone()[0]

print("========== QUESTION N ==========")
print(f"Total number of suppliers: {total_suppliers}")
print()


# ============================================================
# SAVE AND CLOSE
# ============================================================

con.commit()
con.close()

print("================================")
print("Connection Successfully")
print("================================")