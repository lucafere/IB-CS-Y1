import math
print ("Welcome to Luca's Pizzeria!")
people = int(input("Each pizza is 6 slices, how many people will you order for? "))
slices = int(input("How many slices (on average) does each person eat? "))

totalslices = people*slices
totalpizza = totalslices/6
roundedpizza = math.ceil(totalpizza)
extraslices = (6*roundedpizza)-totalslices

print(
    f"Perfect! With {roundedpizza} pizzas you will have enough for everyone "
    f"and you might have {extraslices} extra slices for the next day!"
)
             
