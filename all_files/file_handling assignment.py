# Assignment 1 - Student Registration System

# students = int(input("How many students do you want to register? "))

# with open("students.txt", "w") as file:

#     for i in range(students):
#         print("\nStudent", i + 1)

#         name = input("Full name: ")
#         age = input("Age: ")
#         department = input("Department: ")

#         file.write(f"Name: {name} | Age: {age} | Department: {department}\n")

# print("\nRegistered Students:")

# with open("students.txt", "r") as file:
#     print(file.read())

# file.close()



# Assignment 2- Daily expense tracker

# total = 0

# with open("expenses.txt", "w") as file:

#     while True:
#         item = input("Enter expense item: ")
#         amount = float(input("Enter amount: "))

#         file.write(f"{item} - {amount}\n")

#         total = total + amount

#         choice = input("Do you want to add another expense? (yes/no): ")

#         if choice.lower() == "no":
#             break

# print("\nRecorded Expenses:")

# with open("expenses.txt", "r") as file:
#     print(file.read())

# print("Total amount spent: ₦", total)






# # Assignment 3- Quiz Scores

import csv

students = int(input("How many students? "))

with open("quiz_scores.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Score"])

    for i in range(students):
        name = input("Enter student name: ")
        score = int(input("Enter score: "))

        writer.writerow([name, score])


scores = []

print()
print("Quiz Records:")

with open("quiz_scores.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print()
        print(row[0], "-", row[1])
        scores.append(int(row[1]))


highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

passed = 0

for score in scores:
    if score >= 50:
        passed = passed + 1


print(f"Highest score:, {highest}")
print(f"Lowest score:, {lowest}")
print(f"Average score:, {average}")
print(f"Students who scored 50 and above:, {passed}")

file.close()


