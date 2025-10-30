l =[]
answer = input("Write down any phrase: ")
words = answer.split()
l.append(words)
Max = ""
for x in l:
    for x in words:
        if len(x)>len(Max):
            Max = x
print ("The longest word in your phrase is:",Max)
