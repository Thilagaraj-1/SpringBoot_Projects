first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))
op=(input("enter any operator"))

if op=="+":
    print("Addition:",first+second)
else:
    if op=="-":
        print("Subtraction:",first-second)
    else:
        print("Enter correct input for Subtraction.")
