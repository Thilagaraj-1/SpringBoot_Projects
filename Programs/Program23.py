#While Loop
print("While Loop")
i=1

while i<6:
    print(i)
    i=i+1

#ODD number
print("=========ODD============")    
i=1
while i<11:
    print(i)
    i=i+2

#EVEN number
print("=========EVEN============")
i=0
while i<11:
    print(i)
    i=i+2

#Sum
print("==========SUM===============")
num=int(input("Enter a number : "))
i=1
sum=0

while i<=num:
    sum=sum+i
    i+=1
    print("The sum is : ",sum)
print("The Last Sum : ",sum)

#Factorial
print("===========FACTORIAL=================")
num=int(input("Enter a Number : "))
i=1
fact = 1

while i<=num:
    fact=fact*i
    i+=1
    print("Factorial : ",fact)
print("The Last Factorial : ",fact)
