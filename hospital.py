import sqlite3

# =======
# CONNECT TO DATABASE
# ======

connection = sqlite3.connect("Hospital.db")
cursor = connection.cursor()

# Turn ON Foreign Key support
cursor.execute("PRAGMA foreign_keys = ON")


# ======
# CREATE DOCTORS TABLE
# DoctorID = Primary Key
# ======

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Doctors(
        DoctorID TEXT PRIMARY KEY,
        DoctorName TEXT NOT NULL,
        Specialty TEXT NOT NULL,
        PhoneNumber TEXT
    )
""")


# ============================================================
# CREATE PATIENTS TABLE
# PatientID = Primary Key
# DoctorID = Foreign Key
# ============================================================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients(
        PatientID TEXT PRIMARY KEY,
        PatientName TEXT NOT NULL,
        Age INTEGER,
        DoctorID TEXT,
        FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
    )
""")

# connection.commit()

# ============
# INSERT 8 DOCTORS
# ============

doctors = [
    ("D001", "Dr. Mercy Johnson", "Cardiology", "08012345678"),
    ("D002", "Dr. David Adeyemi", "Pediatrics", "08023456789"),
    ("D003", "Dr. Sarah Williams", "Dermatology", "08034567890"),
    ("D004", "Dr. Michael Brown", "Neurology", "08045678901"),
    ("D005", "Dr. Grace Okafor", "Gynecology", "08056789012"),
    ("D006", "Dr. Daniel Yusuf", "Orthopedics", "08067890123"),
    ("D007", "Dr. Esther Bello", "General Medicine", "08078901234"),
    ("D008", "Dr. James Carter", "Ophthalmology", "08089012345")
]

cursor.executemany("""
    INSERT  OR IGNORE INTO Doctors (DoctorID, DoctorName, Specialty, PhoneNumber)
    VALUES (?, ?, ?, ?)
""", doctors)

# connection.commit()


# ==========
# INSERT 15 PATIENTS
# DoctorID connects each patient to a doctor
# ========

patients = [
    ("P001", "James Ade", 35, "D001"),
    ("P002", "Linda Brown", 28, "D002"),
    ("P003", "Peter Johnson", 42, "D003"),
    ("P004", "Mary Okafor", 19, "D004"),
    ("P005", "David Smith", 51, "D005"),
    ("P006", "Sarah Bello", 33, "D006"),
    ("P007", "John Williams", 25, "D007"),
    ("P008", "Grace Adeyemi", 47, "D008"),
    ("P009", "Daniel Yusuf", 31, "D001"),
    ("P010", "Esther Carter", 22, "D002"),
    ("P011", "Michael Adams", 39, "D003"),
    ("P012", "Faith Johnson", 18, "D004"),
    ("P013", "Samuel Brown", 55, "D005"),
    ("P014", "Deborah James", 29, "D006"),
    ("P015", "Paul Okoro", 44, "D007")
]

cursor.executemany("""
    INSERT OR IGNORE INTO Patients (PatientID, PatientName, Age, DoctorID)
    VALUES (?, ?, ?, ?)
""", patients)

# connection.commit()


# ============
# d. DISPLAY ALL DOCTORS
# ==========

print()
print("========== ALL DOCTORS ==========")

cursor.execute("""
    SELECT * FROM Doctors
""")

for doc in cursor.fetchall():
    doctor_id, doctor_name, specialty, phone_number = doc
    print(
        f"ID: {doctor_id} | "
        f"Name: {doctor_name} | "
        f"Specialty: {specialty} | "
        f"Phone: {phone_number}"
    )


# ================
# e. DISPLAY ALL PATIENTS
# ===============

print()
print("========== ALL PATIENTS ==========")

cursor.execute("""
    SELECT * FROM Patients
""")

for pat in cursor.fetchall():
    patient_id, patient_name, age, doctor_id = pat
    
    print(
        f"ID: {patient_id} | "
        f"Name: {patient_name} | "
        f"Age: {age} | "
        f"Doctor ID: {doctor_id}"
    )


# ==============
# f. PRINT ONLY THE NAMES OF EVERY PATIENT
# ==================

print()
print("========== PATIENT NAMES ==========")

cursor.execute("""
    SELECT PatientName
    FROM Patients
""")

for patient_name in cursor.fetchall():
    print(f"Patient Name: {patient_name[0]}")


# =================
# g. DISPLAY PATIENTS ABOVE 30 YEARS OLD
# ================

print()
print("========== PATIENTS ABOVE 30 ==========")

cursor.execute("""
    SELECT PatientName, Age
    FROM Patients
    WHERE Age > 30
""")

for patient_name, age in cursor.fetchall():
    print(f"Name: {patient_name} | Age: {age}")


# ===================
# h. DISPLAY PATIENT NAME + DOCTOR NAME
# USING INNER JOIN
# ==================

print()
print("========== PATIENTS AND THEIR DOCTORS ==========")

cursor.execute("""
    SELECT Patients.PatientName, Doctors.DoctorName
    FROM Patients
    INNER JOIN Doctors
    ON Patients.DoctorID = Doctors.DoctorID
""")

for patient_name, doctor_name in cursor.fetchall():
    print(f"{patient_name} is assigned to {doctor_name}.")


# ===================
# i. ADD ADDRESS COLUMN TO PATIENTS
# =================

print()
print("========== ADDING ADDRESS COLUMN ==========")

cursor.execute("""
    ALTER TABLE Patients
    ADD COLUMN Address TEXT
""")

connection.commit()

print("Address column added successfully.")


# ========================
# # j. RENAME PatientName TO FullName
# ===========================

print()
print("========== RENAMING PATIENTNAME ==========")

cursor.execute("""
    ALTER TABLE Patients
    RENAME COLUMN PatientName TO FullName
""")

# connection.commit()

print("PatientName has been renamed to FullName.")


# ============================================================
# k. UPDATE PHONE NUMBER OF ONE DOCTOR
# ============================================================

print()
print("========== UPDATING DOCTOR PHONE NUMBER ==========")

cursor.execute("""
    UPDATE Doctors
    SET PhoneNumber = ?
    WHERE DoctorID = ?
""", ("08123456789", "D001"))

connection.commit()

print("Doctor's phone number updated successfully.")


# ============================================================
# l. UPDATE ADDRESS OF THREE PATIENTS
# USING executemany()
# ============================================================

print()
print("========== UPDATING PATIENT ADDRESSES ==========")

addresses = [
    ("Ibadan, Oyo State", "P001"),
    ("Lagos, Lagos State", "P002"),
    ("Abuja, FCT", "P003")
]

cursor.executemany("""
    UPDATE Patients
    SET Address = ?
    WHERE PatientID = ?
""", addresses)

# connection.commit()

print("Three patient addresses updated successfully.")


# ===================
# m. DELETE ONE PATIENT
# ===================

print()
print("========== DELETING ONE PATIENT ==========")

cursor.execute("""
    DELETE FROM Patients
    WHERE PatientID = "PO15"
""")

connection.commit()

print("Patient P015 deleted successfully.")


# ============================
# n. PRINT TOTAL NUMBER OF PATIENTS
# ======================

print()
print("========== TOTAL PATIENTS ==========")

cursor.execute("""
    SELECT COUNT(*)
    FROM Patients
""")

for total_patients in cursor.fetchall():
    print(f"Total number of patients: {total_patients[0]}")


# ====================
# o. PRINT TOTAL NUMBER OF DOCTORS
# =====================

print()
print("========== TOTAL DOCTORS ==========")

# print(cursor.execute("""
#     SELECT COUNT(*)
#     FROM Doctors
# """))

cursor.execute("""
    SELECT COUNT(*)
    FROM Doctors
""")

for total_doctors in cursor.fetchall():
    print(f"Total number of doctors: {total_doctors[0]}")


# ============================================================
# CLOSE DATABASE
# ============================================================

connection.close()

print()
print("========== COMPLETE ==========")
print("Hospital Management System completed successfully.")