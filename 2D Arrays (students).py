students = [
    ['Sophia', 'Taylor', 17, 'F', 'USA', 9, [53, 98, 96, 68, 70, 70, 61, 64]],
    ['Mason', 'Lopez', 18, 'F', 'Japan', 10, [68, 95, 69, 89, 50, 96, 71, 84]],
    ['Mia', 'Taylor', 18, 'M', 'Mexico', 10, [53, 62, 96, 97, 66, 86, 60, 95]],
    ['Luis', 'Taylor', 15, 'M', 'Japan', 10, [94, 91, 64, 90, 84, 98, 100, 59]],
    ['Chloe', 'Johnson', 15, 'F', 'France', 9, [70, 55, 93, 65, 81, 60, 77, 80]],
    ['Isabella', 'Taylor', 16, 'F', 'India', 10, [76, 93, 87, 99, 69, 82, 93, 61]],
    ['Ethan', 'Martinez', 15, 'F', 'India', 10, [56, 77, 66, 96, 96, 76, 94, 63]],
    ['Ava', 'Martinez', 17, 'F', 'Brazil', 10, [85, 99, 85, 96, 92, 52, 96, 96]],
    ['Emma', 'Martinez', 16, 'M', 'Germany', 12, [73, 91, 65, 61, 89, 65, 79, 57]],
    ['Sara', 'Rodriguez', 18, 'F', 'Mexico', 10, [59, 91, 88, 66, 83, 91, 89, 67]],
    ['Liam', 'Rodriguez', 15, 'M', 'Canada', 9, [61, 65, 92, 76, 88, 57, 94, 82]],
    ['James', 'Brown', 17, 'F', 'France', 10, [82, 98, 66, 80, 73, 99, 89, 91]],
    ['Emma', 'Smith', 15, 'F', 'India', 11, [95, 91, 69, 98, 98, 79, 76, 70]],
    ['Sophia', 'Garcia', 17, 'M', 'Japan', 9, [66, 59, 61, 60, 75, 91, 61, 74]],
    ['Ethan', 'Lee', 18, 'M', 'Brazil', 11, [77, 73, 71, 99, 81, 72, 69, 97]],
    ['Isabella', 'Smith', 17, 'M', 'Germany', 11, [78, 95, 81, 86, 78, 89, 83, 83]],
    ['Chloe', 'Johnson', 15, 'M', 'Germany', 9, [93, 77, 66, 55, 60, 82, 60, 61]],
    ['David', 'Lopez', 15, 'F', 'Mexico', 9, [92, 92, 94, 82, 86, 72, 81, 80]],
    ['Lucas', 'Smith', 15, 'F', 'Brazil', 10, [89, 55, 82, 86, 95, 100, 72, 55]],
    ['Ethan', 'Davis', 14, 'M', 'France', 11, [65, 78, 61, 73, 71, 63, 56, 86]],
    ['Ava', 'Lopez', 17, 'F', 'USA', 12, [59, 92, 61, 73, 65, 78, 91, 78]],
    ['Anna', 'Lee', 17, 'M', 'Germany', 12, [72, 99, 64, 94, 56, 98, 99, 59]],
    ['Olivia', 'Davis', 16, 'M', 'India', 11, [75, 69, 99, 68, 65, 96, 83, 91]],
    ['David', 'Lopez', 15, 'M', 'Mexico', 10, [69, 70, 67, 86, 72, 66, 62, 80]],
    ['James', 'Garcia', 14, 'M', 'Japan', 9, [99, 91, 71, 100, 71, 63, 78, 67]],
    ['Emma', 'Lopez', 17, 'F', 'Canada', 10, [65, 67, 83, 82, 75, 70, 79, 78]],
    ['Mason', 'Rodriguez', 18, 'M', 'Mexico', 12, [95, 95, 82, 92, 63, 78, 93, 81]],
    ['James', 'Brown', 16, 'F', 'Brazil', 9, [93, 71, 60, 81, 100, 96, 89, 91]],
    ['John', 'Lee', 16, 'M', 'Germany', 10, [59, 91, 77, 89, 67, 75, 71, 68]],
    ['Sara', 'Martinez', 17, 'F', 'Mexico', 11, [95, 76, 89, 76, 95, 93, 97, 60]]
]


totalstudents = 0
# Total Students 
for x in students:
    totalstudents += 1
print(f"Total amount of students: {totalstudents}")
print("-------------------------------------------------------------")
# Student's per grade
ninegraders = 0
tengraders = 0
elevengraders = 0
twelvegraders = 0
for x in students:
    grade = x[5]
    if grade == 9:
        ninegraders += 1
    elif grade == 10:
        tengraders += 1
    elif grade == 11:
        elevengraders += 1
    elif grade == 12:
        twelvegraders += 1
print("9th graders:",ninegraders)
print("10th graders:",tengraders)
print("11th graders:",elevengraders)
print("12th graders:",twelvegraders)
print("-------------------------------------------------------------")

# Student's Gender
male = 0
female = 0
for x in students:
    sex = x[3]
    if sex == "M":
        male += 1
    elif sex == "F":
        female += 1
print(f"There are {male} male students and {female} female students")
print("-------------------------------------------------------------")

#Student's Nationality 
nationality = []
nationalitycount = []
for x in students:
    if x[4] not in nationality:
        nationality.append(x[4])
        nationalitycount.append(1)
    else:
        place = nationality.index(x[4])
        nationalitycount[place]+=1
    
for x in nationality:
    spot = nationality.index(x)
    print(f"There are {nationalitycount[spot]} students from {nationality[spot]}")

print("-------------------------------------------------------------")

#Average Grades

Math = []
English = []
History = []
Biology = []
Chemistry = []
Physics = []
CompScience = []
PE = []


for x in students:
    Math.append(x[6][0])
    English.append(x[6][1])
    History.append(x[6][2])
    Biology.append(x[6][3])
    Chemistry.append(x[6][4])
    Physics.append(x[6][5])
    CompScience.append(x[6][6])
    PE.append(x[6][7])
print(f"Math average grade: {round(sum(Math)/totalstudents)}")
print(f"English average grade: {round(sum(English)/totalstudents)}")
print(f"History average grade: {round(sum(History)/totalstudents)}")
print(f"Biology average grade: {round(sum(Biology)/totalstudents)}")
print(f"Chemistry average grade: {round(sum(Chemistry)/totalstudents)}")
print(f"Physics average grade: {round(sum(Physics)/totalstudents)}")
print(f"CompScience average grade: {round(sum(CompScience)/totalstudents)}")
print(f"PE average grade: {round(sum(PE)/totalstudents)}")
print("-------------------------------------------------------------")

#Average grade per student
avgrades = []
namess = []
for x in students:
    avgrades.append(round(sum(x[6])/8))
    namess.append(f"{x[0]} {x[1]}")
    print(f"{x[0]} {x[1]}'s average grade is {round(sum(x[6])/8)}")
print("-------------------------------------------------------------")

#Students with highest and lowest averages

studentname = []
studentgrade = []

for x in students:
    studentname.append(f"{x[0]} {x[1]}")
    studentgrade.append(f"{round(sum(x[6])/8)}")
maxindex = studentgrade.index(max(studentgrade))
beststudent = studentname[maxindex]

minindex = studentgrade.index(min(studentgrade))
worststudent = studentname[minindex]

print(f"The best student is {beststudent} with an average grade of {max(studentgrade)}")
print(f"The worst student is {worststudent} with and average grade of {min(studentgrade)}")
print("-------------------------------------------------------------")

#Average grades by sex

malestudentgrades=[]
averagemalegrades = 0
femalestudentgrades=[]
averagefemalegrades = 0

for x in students:
    if x[3] == "M":
        malestudentgrades.append(sum(x[6])/8)
    elif x[3] == "F":
        femalestudentgrades.append(sum(x[6])/8)
        
averagemalegrades = sum(malestudentgrades)/male
averagefemalegrades = sum(femalestudentgrades)/female
print(f"Average male grades: {round(averagemalegrades)}")
print(f"Average female grades: {round(averagefemalegrades)}")
print("-------------------------------------------------------------")

#Average grade by nationality
nationality = []
nationalitygrade = []
for x in students:
    if x[4] not in nationality:
        nationality.append(x[4])
        nationalitygrade.append(sum(x[6])/8)
    else:
        place = nationality.index(x[4])
        nationalitygrade[place] = (nationalitygrade[place] + sum(x[6])/8)/2
for x in nationality:
    spot = nationality.index(x)
    print(f"The average grade of {nationality[spot]} is {round(nationalitygrade[spot])}")
print("-------------------------------------------------------------")


#Students with an average of 90
goodstudents =[]
goodgrade =[]
for x in students:
    if sum(x[6])/8 >= 90:
        goodgrade.append(sum(x[6])/8)
        goodstudent.append(f"{x[0]} {x[1]}")
        
for x in goodstudents:
    place = goodstudents.index(x)
    print(f"{goodstudent[place]} has an average above 90 ({round(goodgrade[place])})")
if goodstudents == []:
    print("No students with average grade over 90")

print("-------------------------------------------------------------")

classes = ["Math", "English", "History", "Biology", "Chemistry", "Physics", "CompScience", "PE"]
grades=[]
grades.append(round(sum(Math)/totalstudents))
grades.append(round(sum(English)/totalstudents))
grades.append(round(sum(History)/totalstudents))
grades.append(round(sum(Biology)/totalstudents))
grades.append(round(sum(Chemistry)/totalstudents))
grades.append(round(sum(Physics)/totalstudents))
grades.append(round(sum(CompScience)/totalstudents))
grades.append(round(sum(PE)/totalstudents))
place = grades.index(min(grades))
print(f"The class with the lowest average is {classes[place]} with a grade of {min(grades)}")
print("-------------------------------------------------------------")
count = 0
print("Top 10 best students:")
for x in range(10):
    best = max(avgrades)
    place = avgrades.index(best)
    count+=1
    print(f"Top {count}: {namess[place]} --> {best}")
    avgrades.pop(place)
    namess.pop(place)

      
            
        



        
