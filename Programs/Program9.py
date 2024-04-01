#Conditional statements
#if else
#if elif else
#i

print("Conditional Statements_if else, if elif else")
print("======================================================")

name = input("Enter your friend name:") 
if name.lower()=="maya":
    print("The name is correct")
elif name.lower()=="muthu":
    print("The name is correct")
elif name.lower()=="rahith":
    print("The name is correct")
else:
    print("The name is wrong")

print("======================================================")

name = input("Enter your Name:")
dept = input("Enter the Dept:")
percent =int(input("Enter the percent:"))

if percent>=90 :
    print("The Grade is A")
elif percent<=89 and percent>=80:
    print("The Grade is B")
elif percent<=79 and percent>=70:
    print("The Grade is C")
else:
    print("You have scored very low marks")

print("Name","Department","Percentage",sep="\t")
print(name,dept,percent,sep="\t")
