import sqlite3


# ================
# CONNECT TO DATABASE
# =======================

connection = sqlite3.connect("Library.db")
cursor = connection.cursor()

# Turn ON Foreign Key support
cursor.execute("PRAGMA foreign_keys = ON")


# ====================
# CREATE BOOKS TABLE
# BookID = Primary Key
# ====================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        BookID TEXT PRIMARY KEY,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL
    )
""")


# ============================================================
# CREATE MEMBERS TABLE
# MemberID = Primary Key
# BorrowedBookID = Foreign Key
# ============================================================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Members(
        MemberID TEXT PRIMARY KEY,
        FullName TEXT NOT NULL,
        BorrowedBookID TEXT,
        FOREIGN KEY (BorrowedBookID) REFERENCES Books(BookID)
    )
""")

# connection.commit()


# ============================================================
# b. INSERT AT LEAST 10 BOOKS
# ============================================================

books = [
    ("B001", "Python for Beginners", "John Smith"),
    ("B002", "Learning SQL", "David Brown"),
    ("B003", "Introduction to Programming", "Sarah Williams"),
    ("B004", "Data Analysis with Python", "Michael Johnson"),
    ("B005", "Web Development Basics", "James Carter"),
    ("B006", "Object Oriented Programming", "Grace Adams"),
    ("B007", "Database Management Systems", "Daniel Okoro"),
    ("B008", "Computer Networks", "Mary Brown"),
    ("B009", "Artificial Intelligence Basics", "Peter Wilson"),
    ("B010", "Software Engineering", "Esther Adeyemi")
]

cursor.executemany("""
    INSERT INTO Books (BookID, Title, Author)
    VALUES (?, ?, ?)
""", books)

# connection.commit()


# ===================
# c. INSERT AT LEAST 12 MEMBERS
# BorrowedBookID connects the member to a book
# =============

members = [
    ("M001", "Mary Johnson", "B001"),
    ("M002", "James Ade", "B002"),
    ("M003", "Sarah Bello", "B003"),
    ("M004", "David Okafor", "B004"),
    ("M005", "Grace Williams", "B005"),
    ("M006", "Daniel Brown", "B006"),
    ("M007", "Esther James", "B007"),
    ("M008", "Michael Adeyemi", "B008"),
    ("M009", "Linda Carter", "B009"),
    ("M010", "John Adams", "B010"),
    ("M011", "Paul Johnson", "B001"),
    ("M012", "Faith Okoro", "B003")
]

cursor.executemany("""
    INSERT INTO Members (MemberID, FullName, BorrowedBookID)
    VALUES (?, ?, ?)
""", members)

# connection.commit()


# d. DISPLAY EVERY BOOK
# =========

print()
print("========== ALL BOOKS ==========")

cursor.execute("""
    SELECT * FROM Books
""")

for book_id, title, author in cursor.fetchall():
    print(
        f"Book ID: {book_id} | "
        f"Title: {title} | "
        f"Author: {author}"
    )


# ================
# e. DISPLAY EVERY MEMBER
# ====================

print()
print("========== ALL MEMBERS ==========")

cursor.execute("""
    SELECT * FROM Members
""")

for member_id, full_name, borrowed_book_id in cursor.fetchall():
    print(
        f"Member ID: {member_id} | "
        f"Name: {full_name} | "
        f"Borrowed Book: {borrowed_book_id}"
    )


# =========
# f. DISPLAY MEMBERS WHO BORROWED A PARTICULAR BOOK
# Example: Python for Beginners
# ========

print()
print("========== MEMBERS WHO BORROWED PYTHON FOR BEGINNERS ==========")

cursor.execute("""
    SELECT Members.FullName
    FROM Members
    INNER JOIN Books
    ON Members.BorrowedBookID = Books.BookID
    WHERE Books.Title = "Python for Beginners"
""")

for member_name in cursor.fetchall():
    print(f"Member: {member_name[0]}")


# ===============
# g. USE INNER JOIN
# Display: Mary Johnson borrowed Python for Beginners
# ====

print()
print("========== MEMBER AND BORROWED BOOK ==========")

cursor.execute("""
    SELECT Members.FullName, Books.Title
    FROM Members
    INNER JOIN Books
    ON Members.BorrowedBookID = Books.BookID
    WHERE Members.FullName = "Mary Johnson"
""")

for member_name, book_title in cursor.fetchall():
    print(f"{member_name} borrowed {book_title}.")


# ==========
# h. ADD EMAIL COLUMN TO MEMBERS
# ==========

print()
print("========== ADDING EMAIL COLUMN ==========")

cursor.execute("""
    ALTER TABLE Members
    ADD COLUMN Email TEXT
""")

connection.commit()

print("Email column added successfully.")


# ===========
# i. RENAME TITLE TO BOOKTITLE
# ===================

print()
print("========== RENAMING TITLE ==========")

cursor.execute("""
    ALTER TABLE Books
    RENAME COLUMN Title TO BookTitle
""")

connection.commit()

print("Title has been renamed to BookTitle.")


# ============
# j. UPDATE EMAIL ADDRESSES OF FIVE MEMBERS
# USING executemany()
# ===

print()
print("========== UPDATING MEMBER EMAILS ==========")

emails = [
    ("ray@gmail.com", "M001"),
    ("jam@gmail.com", "M003"),
    ("goat@gmail.com", "M005"),
    ("champ@gmail.com", "M007"),
    ("lexux10@gmail.com", "M009")
]

cursor.executemany("""
    UPDATE Members
    SET Email = ?
    WHERE MemberID = ?
""", emails)

connection.commit()

print("Five member email addresses updated successfully.")


# ====================
# k. DELETE ONE MEMBER
# ==============================

print()
print("========== DELETING ONE MEMBER ==========")

cursor.execute("""
    DELETE FROM Members
    WHERE MemberID = "M012"
""")

connection.commit()

print("Member M012 deleted successfully.")


# ======================
# l. PRINT TOTAL NUMBER OF BOOKS
# ===============================

print()
print("========== TOTAL BOOKS ==========")

cursor.execute("""
    SELECT COUNT(*)
    FROM Books
""")

for total_books in cursor.fetchall():
    print(f"Total number of books: {total_books[0]}")


# =======================
# m. PRINT TOTAL NUMBER OF MEMBERS
# ========================

print()
print("========== TOTAL MEMBERS ==========")

cursor.execute("""
    SELECT COUNT(*)
    FROM Members
""")

for total_members in cursor.fetchall():
    print(f"Total number of members: {total_members[0]}")


#
# CLOSE DATABASE
# ========================

connection.close()

print()
print("========== COMPLETE ==========")
print("Library Management System completed successfully.")