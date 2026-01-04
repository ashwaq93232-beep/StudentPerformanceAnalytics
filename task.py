# Algorithm to check if a student passes based on their marks

students = ["Ali", "Sara", "Omar", "Laila"]
marks = [65, 48, 70, 55]

for i in range(len(students)):
    mark = marks[i]
    if mark >= 50:
        print(f"{students[i]} passed with {mark} marks.")
    else:
        print(f"{students[i]} failed with {mark} marks.")
