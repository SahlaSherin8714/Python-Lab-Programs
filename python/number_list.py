n=int(input("enter the range"))
numbers=[]
for i in range(n):
    i=int(input("enter the number"))
    if i>100:
        numbers.append('OVER')
    else:
        numbers.append(i)

print(numbers)
