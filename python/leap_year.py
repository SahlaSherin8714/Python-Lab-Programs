#2.Display future leap years from current year to a final year entered by user

start_year=int(input("enter the start year"))
end_year=int(input("enter the end year"))

print("**LEAP YEARS**")
for i in range(start_year,end_year+1):
    if(i%4==0 and i%100 !=0) or (i%400==0):
        print(i)
    
