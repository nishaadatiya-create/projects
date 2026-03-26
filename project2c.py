num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

if num1>num2 or num1>num3:
    print(f"{num1} is largest number among {num1 , num2 ,num3}")
    
elif num2>num3:
    print(f"{num2} is largest number among {num1 , num2 ,num3} ")
    
else:
    print(f"{num3} is largest number among {num1 , num2 ,num3}")