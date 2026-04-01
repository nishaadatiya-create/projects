students = []

while True:
    print("\nWelcome to Student Data Organizer!\n")

    print("Enter 1 to Add Student")
    print("Enter 2 to View All Students")
    print("Enter 3 to Delete Student")
    print("Enter 4 to Update Student")
    print("Enter 5 to Display Subjects")
    print("Enter 0 to Exit\n")

    choice = int(input("Enter your choice: "))

    match choice:

    
        case 1:
            st = {
                "id": input("Enter Student ID: "),
                "name": input("Enter Name: "),
                "age": int(input("Enter Age: ")),
                "grade": input("Enter Grade: "),
                "dob": input("Enter DOB: "),
                "subjects": set(input("Enter Subjects (comma separated): ").split(","))
            }

            students.append(st)
            print("\nStudent added successfully!\n")

        case 2:
            if not students:
                print("\nNo students found\n")
            else:
                for st in students:
                    print(f"ID: {st['id']} | Name: {st['name']} | Age: {st['age']} | Grade: {st['grade']} | Subjects: {', '.join(st['subjects'])}")

     
        case 3:
            sid = input("Enter Student ID to delete: ")
            found = False

            for st in students:
                if st['id'] == sid:
                    students.remove(st)
                    print("Student deleted successfully!")
                    found = True
                    break

            if not found:
                print("Student not found!")

       
        case 4:
            sid = input("Enter Student ID to update: ")
            found = False

            for st in students:
                if st['id'] == sid:
                    found = True

                    print("1. Update Age")
                    print("2. Update Subjects")

                    ch = int(input("Enter choice: "))

                    if ch == 1:
                        st['age'] = int(input("Enter new age: "))
                        print("Age updated!")

                    elif ch == 2:
                        st['subjects'] = set(input("Enter new subjects: ").split(","))
                        print("Subjects updated!")

                    break

            if not found:
                print("Student not found!")

      
        case 5:
            all_subjects = set()

            for st in students:
                all_subjects.update(st['subjects'])

            print("\nSubjects Offered:")
            for sub in all_subjects:
                print(sub.strip())

        
        case 0:
            print("\nGood bye!\n")
            break

        case _:
            print("\nInvalid choice\n")