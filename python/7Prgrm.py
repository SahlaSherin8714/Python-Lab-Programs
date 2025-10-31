lst1=[1,2,3,30]
lst2=[6,7,3,9,11,2]
same_lst=[]
if len(lst1)==len(lst2):
    print("length of two lists are same( ",len(lst1),')')
else:
    print("length of lists are not same")


if sum(lst1)==sum(lst2):
    print("sum of two lists are same( ",sum(lst1),')')
else:
    print("sum of lists are not same")


for i in lst1:
    if i in lst2:
        print(i,"present in both lists")
    else:
        print(i,"not prsent")
        
