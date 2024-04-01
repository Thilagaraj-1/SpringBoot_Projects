#Tuple
tup=(1,2,3,4,5,5)
tup2=(6,7,8,9)

print("Indexing")
print(tup[1])
print("Slicing")
print(tup[:2])
print("Concodinate")
tup3=tup+tup2
print(tup3)

print(tup.count(5))
print(tup.index(3))

print(max(tup2))
print(min(tup2))

#Reverse
print(tup3[::-1])

color="Red"
print(color[::-1])

#Unpacking

tup4=(1,2,3,4,5)

a,b,c,d,e = tup4
print(a)
print(b)
print(c)
print(d)
print(e)

f,g,*h = tup2
print(h)

#Changes tuple to list and list to tuple
tup5=(1,2,3,4,5)
a=list(tup5)
a.remove(3)
tup5=tuple(a)
print("Tuple : ",tup5)
