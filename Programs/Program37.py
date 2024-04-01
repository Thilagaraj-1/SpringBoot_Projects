List1=[10,20,30,40,50]
sum=0
for i in List1:
    print(i)
    sum=sum+i
print("Sum is : ",sum )

List2=[10,20,30]

print(List2)
List2.insert(1,'ABC')
print(List2)
List2.insert(3,'PQR')
print(List2)
List2.insert(5,'PQR')
print(List2)
List2.insert(5,99)
print(List2)

List3=[10,20,30,40,30]

print(List3)
List3.pop(2)
print(List3)
List3.pop(0)
print(List3)

List4=[10,20,10,30,10,40,10,50]
num=int(input("Enter any Number : "))

if num in List4:
    List4.remove(num)
else:
    print

print(List4)

List5=[10,20,30,40,50]

List5.pop(1)
List5.pop(1)
print(List5)




