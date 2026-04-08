print("----- Python OOP Project : Employee Management System------\n")

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        print(f"\n Employeee created with name :{self.name} age :{self.age} salary: {self.salary}\n")


    def display(self):
        print(f"\n Employee Details :\n Name: {self.name}\n Age: {self.age}\n Salary: {self.salary}\n")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
        print(f"\n Manager created with name :{self.name} age:{self.age} salary:{self.salary} department :{self.department}\n")

    def display(self):   
        super().display()
        print(f"\nManager Details : \n Name: {self.name}\n Age: {self.age}\n Salary: {self.salary} \n Department :{self.department}")


class Developer(Employee):
    def __init__(self, name, age, salary, programming):
        super().__init__(name, age, salary)
        self.programming = programming
        print(f"\n Devloper created with name:{self.name} age:{self.age} salary:{self.salary} Programming Language:{self.programming}\n")

    def display(self):  
        super().display()
        print(f"\nDeveloper Details :\n Name: {self.name}\n Age: {self.age}\n Salary: {self.salary} \n Prpgramming Language:{self.programming}")


e_list=[]
m_list=[]
d_list=[]

while True:
    print("Choose an Operation")
    print("\n1. Create a Employee")
    print("2. Create a Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Exit\n")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("enter name :")
            age = input("enter age: ")
            salary = input("enetr salary:")
            e_list.append(Employee(name,age,salary))
        case 2:
            name = input("enter name :")
            age = input("enter age: ")
            salary = input("enetr salary:")
            department= input("enter department:")
            m_list.append(Manager(name,age,salary,department))
        case 3 :
            name = input("enter name :")
            age = input("enter age: ")
            salary = input("enetr salary:")
            programming=input("enter programming language:")
            d_list.append(Developer(name,age,salary,programming))   
        case 4 :
            print("\nChoose details to show:\n 1. Employee \n 2. Manager \n 3. Developer")
            ch = int(input("Enter your choice :"))

            if ch==1:
                for e in e_list:
                    e.display()
            elif ch==2:
                for m in m_list:
                    m.display()
            elif ch==3:
                for d in d_list:
                    d.display()

            else :
                print("Invalid choice")
                
        case 5 :
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!\n")
            break
        
        