L1=[4,5,6,7,11,13,15,16]
L2=[0,2,3,58,78,79,100]
L3=[]

for i in L1:
    if i not in L3:
        L3.append(i)

for i in L2:
    if i not in L3:
        L3.append(i)

L3.sort()
print(L3)


maxsequence = []
subsequence = []
previous = 0

for num in L3:
    if num == previous + 1:
        subsequence.append(num)
    else:
        if len(subsequence) > len(maxsequence):
            maxsequence = subsequence[:]
        subsequence = [num]
    previous = num

if len(subsequence) > len(maxsequence):
    maxsequence = subsequence[:]

print(maxsequence)
        
        
        
        
    
    
        
        
            
            
        
        



