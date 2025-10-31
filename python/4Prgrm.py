string=input("enter the string:")
words=string.split()
count_words=[]
counts=[]

for w in words:
    if w not in count_words:
        count=0
        for i in words:
            if i==w:
                count+=1
        count_words.append(w)
        counts.append(count)
        
for l in range(len(count_words)):
    print(count_words[l],' : ',counts[l])
