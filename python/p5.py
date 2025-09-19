number=[3,1,4,9,8,2,6]
print("length of string:",len(number))
print("last element of string:",number[-1])
number.reverse()
print("reverse of string:",number)
if 9 in number:
    print(True)
number.insert(7,7)
print("last list after adding element 7:",number)
