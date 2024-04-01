a={1,2,3,4}
b={5,6,7}

print("Disjoint : ",a.isdisjoint(b))

x={1,2,3,4}
y={3,4,5,6}

print("Disjoint : ",y.isdisjoint(x))

a={1,2,3}
b={1,2,3,4,5}

print("Subset : ",a.issubset(b))

x={1,2,3}
y={1,3,4,5}

print("Subset : ",x.issubset(y))

x={1,2,3,4,5,6}
y={3,4}

print("Superset : ",x.issuperset(y))
print("Superset : ",y.issuperset(x))
