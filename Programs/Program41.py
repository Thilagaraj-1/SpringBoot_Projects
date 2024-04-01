a={1,2,3,4}
b={3,4,5,6}

c=a.union(b)
print("Union : ",c)

d=a.intersection(b)
print("Intersection : ",d)

e=a.difference(b)
print("Difference of a : ",e)

f=b.difference(a)
print("Difference of b : ",f)

g=a.symmetric_difference(b)
print("Symmetric Difference of a and b : ",g)

a.symmetric_difference_update(b)
print("Symmetric difference_update : ",a)   

a.intersection_update(b)
print("Intersection_update of a : ",a)

print("--------------------------------")

x={10,20,30}
y={30,40,50}
x.symmetric_difference_update(y)
print("Symmetric_difference_update : ",x)
