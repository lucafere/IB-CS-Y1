import os

infile = open("secondarystudents.text","r") 
outfile = open("correctedstudents.txt","w")
aline = infile.readline()
while aline:
    items = aline.split(",")
    if items[3].lower() == "uyu" or items[3].lower() == "uru" or items[3].lower() == "ury" or items[3].lower() == "uruguay":
        items[3] = "Uruguayan"
    outfile.write(",".join(items))
    aline = infile.readline()
infile.close()
outfile.close()
os.replace("correctedstudents.txt", "secondarystudents.text")
print("File updated")
