name = input("Enter your Name:")
address = input("Enter the address:")
age =int(input("Enter the age:"))
gender=input("Enter your Gender:")

t1="5 rupees"
t2="10 rupees"

if age<=11 and age>0:
   print("Name","Address","Age","Gender","tprice",sep="\t")
   print(name,address,age,gender,t1,sep="\t")
elif age>=12 and age<=70:
    print("Name","Address","Age","Gender","tprice",sep="\t")
    print(name,address,age,gender,t2,sep="\t")
elif age>=71:
    print("Name","Address","Age","Gender","tprice",sep="\t")
    print(name,address,age,gender,t1,sep="\t")
elif age==0:
    print("0 is not an age")
else:
    print("Enter Your Correct Age")

print("=============================================")


