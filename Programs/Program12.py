
name=input("Enter your Name:")
age=int(input("Enter Your Age:"))
salary=int(input("Enter your Monthly Salary:"))
loan=int(input("Enter your Loan amount:"))
print("========================================================")
if age>=18:
    print("Your age is eligible.")
    print("========================================================")
    #salary=int(input("Enter your Monthly Salary:"))
    if salary<=10000:
        print("Your salary is eligible to take loan.")
        print("========================================================")
        #loan=int(input("Enter your Loan amount:"))
        if loan<=50000:
            print("Your Loan has Approved.")
            print("Name","Age","Salary","Loan Amount",sep="\t\t")
            print(name,age,salary,loan,"eligible",sep="\t\t")
        else:
            print("Your Loan amount exceeds the limit.")
            print("Name","Age","Salary","Loan Amount",sep="\t\t")
            print(name,age,salary,loan,"Not eligible",sep="\t\t")
    else:
        print("Your salary is not eligible to take loan.")
        print("==================================================================")
        print("Name","Age","Salary","Loan Amount",sep="\t\t")
        print(name,age,salary,loan,"not eligible",sep="\t\t")
else:
    print("You are minor.")
    print("Name","Age","Salary","Loan Amount",sep="\t\t")
    print(name,age,salary,loan,"Not eligible",sep="\t\t")
    

print("=================================================================")
