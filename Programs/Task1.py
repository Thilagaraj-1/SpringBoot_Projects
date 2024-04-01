print("=======================================================")
lim=int(input("Enter an Number : "))
list=[]
for i in range(lim):
    Integer=int(input("Enter an Integer : "))
    list.append(Integer)

print(list)

print("=======================================================")
print("Delete Duplicate Values")
list1=[10,20,10,20,30,40,30,50]
list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print
        
print(list2)

print("=======================================================")

start=int(input("Enter a Start Integer : "))
end=int(input("Enter an End Integer : "))

list=[]
square=[]
cube=[]

for i in range(start,end+1):
    list.append(i)
    square.append(i*i)
    cube.append(i**3)
    
print("List : ",list)
print("Square : ",square)
print("Cube : ",cube)

print("=======================================================")
list = [10,20,30,40,50,60]
list1 = list[0:3]
list2 = list[3:]

print("List1 : ",list1)
print("List2 : ",list2)

print("=======================================================")
str = "12345"

list = []

for i in str:
    x=int(i)
    list.append(x)
print(list)

print("=======================================================")
Input = input("Enter String Value : ")
list1=[]

for i in Input:
    if x in i:
        y=int(x)
        list1.append(y)
    else:
        print("ValueError")

print(list1)
