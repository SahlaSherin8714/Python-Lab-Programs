dict1={'mark1':100,'mark2':65,'mark3':70}
dict2={'mark5':95,'mark6':60}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)


n=int(input("enter a number"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

#summ of all items in dictionary
dic1=dict(m1=40,m2=30,m3=50)
sum1=0
for i in dic1.values():
    sum1+=i
print(sum1)

#product of all items in dictionary
dic=dict(a=1,b=2,c=6)
prod=1
for i in dic.values():
    prod*=i
print(prod)
