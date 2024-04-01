#1)
'''num = int(input("Enter a number you want to sum : "))
sum=0

while num>0:
    action = num%10
    sum +=action
    num = num//10
print(sum)'''

#2)
'''num = int(input("Enter a number : "))
if num%2==0 and num%3==0:
    print("The Given number is divisible by 2 and 3")
elif num%2==0:
    print("The Given number is divisible by 2 not 3")
elif num%3==0:
    print("The Given number is divisible by 3 not 2")
else:
    print("The Given number is not divisible by 2 and 3")'''

#3)
'''num = int(input("Enter a number : "))
for i in range(1,num + 1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

#4)
'''row = int(input("Enter a number : "))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''


#5)
row = 9 
for i in range(1,row+1,2):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,row+1,2):
    print(" "*(row-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
