
list1=[[1,2,3],[1,2,3],[1,2,3]]
tup1=((4,5,6),(4,5,6),(4,5,6))

print("===========list operation===============")
for i in list1:
    for j in i:
        print(j)
print("===========tuple operation===============")
for i in tup1:
    for j in i:
        print(j)

print("----------------Nested Dictionary iteration--------------------------") 

Sivakumar={"Surya":{"name":"Surya","Age":40,"isMarried":True},
           "Karthi":{"name":"Karthi","Age":38,"isMarried":False}}



for i,j in Sivakumar.items():
    print(i)
    for k,l in j.items():
        print("\t",k,":",l)
    print()
        
