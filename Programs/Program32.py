#TEST-1

#1)
String=input("Enter : ")
print(String[::-1])

#2)
count=0
cv = input("Enter : ")
vowels = 'aeiou'



for i in cv:
    if i in vowels:
        count = count+1
    else:
        print('')
print(count)

#3)
pal =input("Enter : ")
x=(pal[::-1])
if x==pal:
    print('True')
else:
    print('False')


#4)
st =input("Enter : ")
print(st.swapcase())

#5)
cap =input("Enter : ")
print(cap.title())

#6)
rs=input("Enter : ")
print(rs.replace(" ",""))

#7)
ew =input("Enter : ")
print(ew.endswith("world"))

#8)
rep =input("Enter : ")
print(rep.replace("world","Python"))

#Goodwin>3)
x =input("Enter : ")
y =x.lower()

a = y.count('a')
b = y.count('e')
c = y.count('i')
d = y.count('o')
e = y.count('u')

print(a + b + c + d + e)


