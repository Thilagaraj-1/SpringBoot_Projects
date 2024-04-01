x = int(input("Enter which table : "))
limit = int(input("Enter your limit for table: "))
print("------- Here your",x,"table of",limit,"--------")
for i in range (1,limit+1):
    table=x*i
    print(x,"*",i,"=",table)
    
