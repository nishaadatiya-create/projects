age=int(input("ENter your Age:"))

if age==0 or age<=12:
    print("Child")
    
elif age>=13 or age==19:
    print("Teenage")
    
# elif age<=20 or age==59:
#     print("Adult")
    
else:
    print("Senior")