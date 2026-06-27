student = {}

def add_student(name, marks):
    student[name] = marks
    return "successful"

def view_students():
    if not student:
        return "📭 No Students Available!"

    for count, (name, marks) in enumerate(student.items(), start=1):
        print(f"{count}. {name}: {marks}")
    return None
    
def search_student(name):
    if name in student:
        return student[name]
    return None


def delete_student(name):
    if name in student:
        del student[name]
        return "successful"
    return "❌ Student Not Found"

def update_student_marks(name, marks):
    if name in student:
        student[name] = marks
        return "successful"
    return "❌ Student Not Found"

while True:
    print("📚 ===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Exit")

    try:
        choice = int(input("Enter the Choice (1-6): "))
    except ValueError:
        print("❌ Please enter a valid number between 1 and 6.")
        continue

    if choice == 6:
        print("👋 Thank you for using Student Management System!")
        break

    if choice == 1:
        name = input("Enter the name: ")
        try:
            marks = int(input("Enter the marks: "))
        except ValueError:
            print("❌ Marks must be a number.")
            continue

        if marks < 0 or marks > 100:
            print("❌ Marks should be between 0 and 100.")
        else:
            print("✅", add_student(name, marks))

    elif choice == 2:
        result = view_students()
        if result:
            print(result)

    elif choice == 3:
        name = input("Enter the name: ")
        result = search_student(name)
        if result is None:
            print("❌ Student Not Found")
        else:
            print(f"🔍 {name}: {result}")

    elif choice == 4:
        name = input("Enter the name: ")
        result = delete_student(name)
        print("🗑️", result)

    elif choice == 5:
        name = input("Enter the name whose marks you want to update: ")
        try:
            marks = int(input("Enter the new marks: "))
        except ValueError:
            print("❌ Marks must be a number.")
            continue

        if marks < 0 or marks > 100:
            print("❌ Marks should be between 0 and 100.")
        else:
            print("✅", update_student_marks(name, marks))

    else:
        print("❌ Please choose a valid option between 1 and 6.")

