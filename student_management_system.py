student = {}

def add_student(name, marks):
    student[name] = marks
    return "Student Added Successfully! 🎉"

def view_students():
    if not student:
        return "📭 No Students Available in the System!"

    print("\n📋 ====== CURRENT STUDENT LIST ======")
    for count, (name, marks) in enumerate(student.items(), start=1):
        print(f"🔹 {count}. {name:<15} ✨ Marks: {marks}")
    print("=====================================")
    return None
    
def search_student(name):
    if name in student:
        return student[name]
    return None

def delete_student(name):
    if name in student:
        del student[name]
        return "Student Deleted Successfully! 🗑️"
    return "❌ Student Not Found"

def update_student_marks(name, marks):
    if name in student:
        student[name] = marks
        return "Marks Updated Successfully! 🔄"
    return "❌ Student Not Found"

while True:
    print("\n🎓 ===================================== 🎓")
    print("📚       STUDENT MANAGEMENT SYSTEM       📚")
    print("🎓 ===================================== 🎓")
    print("📌  1. ➕ Add Student")
    print("📌  2. 📋 View Students")
    print("📌  3. 🔍 Search Student")
    print("📌  4. 🗑️ Delete Student")
    print("📌  5. 🔄 Update Marks")
    print("📌  6. 🚪 Exit")
    print("=========================================")

    try:
        choice = int(input("👉 Enter your Choice (1-6): "))
    except ValueError:
        print("\n⚠️  Error: Please enter a valid number between 1 and 6.")
        continue

    if choice == 6:
        print("\n👋 Thank you for using Student Management System! Goodbye!")
        break

    if choice == 1:
        name = input("👤 Enter student name: ")
        try:
            marks = int(input("💯 Enter student marks: "))
        except ValueError:
            print("\n⚠️  Error: Marks must be a number.")
            continue

        if marks < 0 or marks > 100:
            print("\n⚠️  Error: Marks should be between 0 and 100.")
        else:
            print(f"\n✅ {add_student(name, marks)}")

    elif choice == 2:
        result = view_students()
        if result:
            print(f"\n{result}")

    elif choice == 3:
        name = input("🔍 Enter the name to search: ")
        result = search_student(name)
        if result is None:
            print("\n❌ Student Not Found")
        else:
            print(f"\n✨ Result Found:")
            print(f"👤 Name: {name} | 💯 Marks: {result}")

    elif choice == 4:
        name = input("🗑️ Enter the name to delete: ")
        result = delete_student(name)
        if "Successfully" in result:
            print(f"\n✅ {result}")
        else:
            print(f"\n{result}")

    elif choice == 5:
        name = input("🔄 Enter the name to update marks: ")
        try:
            marks = int(input("💯 Enter the new marks: "))
        except ValueError:
            print("\n⚠️  Error: Marks must be a number.")
            continue

        if marks < 0 or marks > 100:
            print("\n⚠️  Error: Marks should be between 0 and 100.")
        else:
            result = update_student_marks(name, marks)
            if "Successfully" in result:
                print(f"\n✅ {result}")
            else:
                print(f"\n{result}")

    else:
        print("\n⚠️  Error: Please choose a valid option between 1 and 6.") aab kaisa lag rha hai rate karna
