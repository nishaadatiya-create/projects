print("==============================================")
print("Welcome to Multi-Utility Toolkit")
print("==============================================")
while True:
    print("Enter Any Number between 1 to 7:")
    print("1. Datatime and Time Operations \n2. Mathematical operation \n3. Random Data Generation \n4. Generate Unique Identifiers (UUID)\n5. File operations (custom Module)\n6. Explore Module Attributes (dir())\n7. Exit")
    print("==============================================")
    choice =int(input("Enter your Choice:")) 

    match choice:
        
        case 1:
    
            print("Datetime and Time operation:\n1. Display current date and time\n2. Calculate difference between two dates/times\n3. Format date into custom format\n4. Stopwatch\n5. Countdown\n6. Back to Main Menu\n")
            ch= int(input("enter your choice:"))
            if(ch==1):
                import datetime
                now = datetime.datetime.now()
                print("Current Date & Time:", now)
                print("\n")
                
            elif(ch==2):
                from datetime import datetime
                start = datetime(2026, 4, 28, 10, 30)
                end = datetime(2026, 5, 1, 14, 45)
                diff = end - start
                print("Difference:", diff)
                
            elif(ch==3):
                import datetime
                custom_date = datetime.datetime(2024, 10, 5, 12, 30, 45)
                print("Custom Date & Time:", custom_date)
                
            elif(ch==4):
                import time

                input("Press ENTER to start stopwatch...")
                start_time = time.time()

                input("Press ENTER to stop stopwatch...")
                end_time = time.time()

                elapsed_time = end_time - start_time
                print(f"Elapsed Time: {elapsed_time:.2f} seconds")
                
            elif(ch==5):
                import time

                seconds = int(input("Enter time in seconds: "))

                while seconds > 0:
                    print("Time left:", seconds, "seconds")
                    time.sleep(1)
                    seconds -= 1

                print("Time's up!")
                
                
            elif(ch==6):
                print("Back to Main menu")
                
            
            else:
                print("Invalid Choice!")
            
            
                                
        case 2:
            print("Mathematical Operation\n")
            print("1. Calculate Factorial\n 2. Solve Compund Interest\n3. Trignometric Calculations\n4. Area of Geometric Shapes\n5. BAck to main menu")
            ch =int(input("Enter your choice:"))
            if(ch==1):
                import math
                no=int(input("enter a number:"))
                print(math.factorial(no))
                
            elif(ch==2):
                P = float(input("Enter principal amount: "))
                r = float(input("Enter annual interest rate (%): ")) / 100
                t = float(input("Enter time (years): "))
                n = int(input("Enter number of times interest is compounded per year: "))

                A = P * (1 + r/n) ** (n*t)
                CI = A - P

                print("Final Amount:", round(A, 2))
                print("Compound Interest:", round(CI, 2))
                
            elif(ch==3):
                import math
                print(math.sin(math.radians(30)))  
                print(math.cos(math.radians(60)))  
                print(math.tan(math.radians(45))) 
                
            elif(ch==4):
                import math

                
                print("\n--- Area Calculator ---")
                print("1. Circle")
                print("2. Rectangle")
                print("3. Square")
                print("4. Triangle")
                print("5. Exit")

                choice = input("Choose shape: ")

                if choice == "1":
                    r = float(input("Enter radius: "))
                    area = math.pi * r * r
                    print("Area of Circle:", round(area, 2))

                elif choice == "2":
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    area = l * w
                    print("Area of Rectangle:", area)
                    
                elif choice == "3":
                    a = float(input("Enter side: "))
                    area = a * a
                    print("Area of Square:", area)

                elif choice == "4":
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))
                    area = 0.5 * b * h
                    print("Area of Triangle:", area)

                else:
                    print("Invalid choice!")
                        
            elif(ch==5):
                print("Back to Main Menu\n")
                
            
            else:
                print("Invalid choice!")
                
                
        case 3:
            print("Random Data Generation\n1. Generate Random Number\n2. Generate Random List\n3. Create Random Password\n4. Generate Random OTP\n5. Back to Main Menu\n")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                import random
                print(random.random())  
                
            elif(ch==2):
                import random
                fruits = ["apple", "banana", "cherry", "mango"]
                print(random.choice(fruits)) 
                
            elif(ch==3):
                import random
                print(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*', k=10)))
                
            
            elif(ch==4):
                import random
                print(random.randint(100000, 999999))
            
            elif(ch==5):
                print("Back to main Menu")
                break
            
            else:
                print("Invalid choice!")
            
        case 4:
            import uuid
            print("Generate unique Indentifiers:\nGenerated +UUId :")
            print(uuid.uuid4())
            
    
        case 5:
            print("File Operations:\n1. Create a new file\n2.Write to a file\n3. Read from a file\n4. Append to a file\n5.Back to Main Menu")
            ch=int(input("Enter Your Choice:"))
            if(ch==1):
               open("file.txt", "w").close()
                
            elif(ch==2):
                open("file.txt", "w").write("Hello World")
                print("Data written successfully!")
            elif(ch==3):
                print(open("file.txt", "r").read())
            elif(ch==4):
                open("file.txt", "a").write(" More text")
            elif(ch==5):
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice!")
        
        case 6:
            m = __import__(input("Enter module name: "))
            print(dir(m))
            
        
        case 7:
            print("========================================")
            print("Thank you for Using The Multi-Utility Toolkit!")
            print("========================================")
            break
        
        case _:
            print("Invalid Choice!")
            
                    
            

                    
            
        
                
                
                
                
                                
                
   
    

    