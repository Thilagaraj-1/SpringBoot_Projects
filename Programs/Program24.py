num = int(input("Enter a number : "))

empty = 0

while num>0:
    server = num%10
    empty = empty*10+server
    num = num//10
print(empty)
