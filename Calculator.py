l=[]
def calc():
    print('''Enter:
             1 to Add
             2 to Substract
             3 to Multiply
             4 to Divide
             5 to Get History
             6 to Exit''')
    while True:
        c=input("Enter from 1 to 6:")
        if c=="1":
            n=float(input("Enter first number for addition: "))
            m=float(input("Enter second number: "))
            d=n+m
            l.append(str(n) + " + " + str(m) + " = " + str(d))
            print(d,"is the sum.")
        elif c=="2":
            n=float(input("Enter first number for subtraction: "))
            m=float(input("Enter second number: "))
            d=n-m
            l.append(str(n) + " - " + str(m) + " = " + str(d))
            print(d,"is the subtraction.")
        elif c=="3":
            n=float(input("Enter first number for multiplication: "))
            m=float(input("Enter second number: "))
            d=n*m
            l.append(str(n) + " * " + str(m) + " = " + str(d))
            print(d,"is the multiplication")
        elif c=="4":
            n=float(input("Enter first number for division: "))
            m=float(input("Enter second number: "))
            if m==0:
                print("division by zero is not allowed")
            else:
                d=n/m
                l.append(str(n) + " / " + str(m) + " = " + str(d))
                print(d,"is the division.")
        elif c=="5":
            for i in l:
                print(i)
        elif c=="6":
            break
calc()
