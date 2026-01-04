students = ["Ahmed", "Sara", "Ali"]
marks = [85, 45, 90]
for i in range(len(students)):
    mark = marks[i]
    if mark >= 60:  # غيرنا شرط النجاح من 50 إلى 60
        print(f"{students[i]} passed with {mark} marks. Congratulations!")
    else:
        print(f"{students[i]} failed with {mark} marks. Better luck next time.")