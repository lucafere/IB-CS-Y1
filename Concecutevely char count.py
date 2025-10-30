word= input("Write a word: ")
count=0
char=""
maxcount=0
maxchar=""

for x in word:
    if x !=char:
        char=x
        count=1
        
    else:
        count+=1

    if count>maxcount:
        maxcount=count
        maxchar=char
print("The character that was consecutevely repeated the most was",maxchar,"for a total amount of",maxcount"times")
