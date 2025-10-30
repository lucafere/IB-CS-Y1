word=input("Write down word: ")
vowel= ("a", "e", "i", "o", "u")
current = 0
best = 0
L=[]
S=[]
for x in word:
    if x in vowel:
        current += 1
        L.append(x)
    if current > best:
        best =  current
        S = L[:]
    else:
        current = 0
        L.clear()
        
print("The longest consecutive string of vowels was",best,"and it was the vowels","".join(S))

Beautiful
