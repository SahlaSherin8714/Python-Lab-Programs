names=['Anna','sarah','vinu','sahla','Arathi']
a_list=[]
for i in names:
    count=0
    for j in i:
        j=j.lower()
        a_list.append(j)
        
for  k in a_list:   
    if k=='a':
        count +=1
        
print('count of a is : ',count)
        
        

        


