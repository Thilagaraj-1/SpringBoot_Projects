print("----------------list,tuple iteration-------------")
list1=[1,2,3]
tup1=(1,2,3)

for i in list1:
    print(i)

for g in tup1:
    print(g)
print("----------------Object iteration-------------")
dic1={
    "name":"naresh",
    "age":19,
    "city":"mdu"
    }

for i in dic1.values():
    print(i)

for i in dic1.items():
    print(i)

for a,b in dic1.items():
    print(a,"\t : \t",b)

