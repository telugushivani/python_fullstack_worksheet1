try: 
    num1=int(input("Entet First Number:"))
    
    num2=int(input("Entet second  Number:"))

  
    total=num1/num2
    print(total)
except ZeroDivisionError:
    print("cannot divided by zero")    
except ValueError:
    print("please enter integer")
