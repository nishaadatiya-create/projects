print("Welcome to the Pattern Generator and Number Analyzer!")


while True:
    print("Select an Option")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice =int( input("Enter your choice :"))
    
    match choice:
        case 1:
            print("Pattern")
            for i in range(1,5+1):
                for j in range(i):
                    print("*",end=" ")
                print()
                    
                
        case 2:
            pass
        case 3:
             pass


    



