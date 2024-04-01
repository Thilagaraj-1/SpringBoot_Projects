#Set

s={"apple","orange",0,2,3,2,3,True,False}
print(s)

List=["apple","orange","apple",1,2,3,True,False]
rd = set(List)
print("Remove duplicates : ",rd)

set={1,2,3}

set.add(4)
print("Add : ",set)
set.remove(2)
print("Remove : ",set)

a={"Grapes",5}
set.update(a)
print("Update : ",set)


set.discard(6)
print("Discard : ",set)

