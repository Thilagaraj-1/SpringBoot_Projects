#List

list = [1,"apple",1.43,True]

print(list)
print(type(list))

a=str(2)
print(type(a))

b=[1,2.0,"apple",True]
print("Length is : ",len(b))
for i in b:
    print(i)
    
a=[1,2,3,4,"apple"]

print(a[::3])

list1=[1,2,3,4,5,'apple',1,2,3]
print(list1[::-1])

print("=======================ADD============================")
#ADD
#Append
list2=[1,2,3,4,5]
list2.append(6)
print("Append : ", list2)
#insert
list2.insert(1,"list")
print("Insert : ", list2)
#Extend
list1.extend(list2)
list1.extend([7,8])
print("Extend : ",list1)

print("=======================REmOVE============================")
#Remove
list1.remove('apple')
print("remove() : ",list1)
#Pop
list1.pop(8)
print("pop() : ",list1)
#Clear
list2.clear()
print("clear(): ",list2)
#delete
del list2
print(list1)
