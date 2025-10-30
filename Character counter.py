word= input("Write down word: ")
L=[]
N=[]
for x in word:
    if x not in L:
        L.append(x)
        N.append(1)
    else:
        N[L.index(x)]+=1
maxn = max(N)
maxl = L[N.index(maxn)]

print("The most repeated character is",maxl,"and it appears",maxn)
        
