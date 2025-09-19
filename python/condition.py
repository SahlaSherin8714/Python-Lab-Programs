#check the number is EVEN OR ODD

a=int(input("enter the number:"))
if a%2==0:
    print(a," is even")
else:
    print(a,"is odd")

#check a number is POSITIVE , NEGATIVE OR ZERO

num=int(input("enter the number:"))
if num<0:
    print("number is negative")
elif num==0:
    print("number is zero")
else:
    print("number is positive")

#Take a mark check the student is PASSED OR FAILED (mark>=40 pass)

mark=int(input("enter the mark:"))
if mark>=40:
    print("You passed")
else:
    print("You failed")

