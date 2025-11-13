# 2D Array Challenge
# Sample 6x6 matrix for testing

matrix = [
    [12, 7, 9, 21, 5, 14],
    [8, 19, 3, 10, 6, 11],
    [4, 16, 25, 2, 13, 17],
    [9, 5, 18, 20, 7, 15],
    [6, 22, 1, 14, 8, 10],
    [11, 3, 12, 19, 9, 24]
]

# Exercise 1: Count values in a given range : Write a function that returns how many numbers
# in the matrix are between low and high (inclusive).

def inrange(matrix, low, high):
    value = 0
    count = 0
    for x in matrix:
        for y in x:
            if high >= y >= low:
                count += 1
    print(f"There are {count} values in between {low} and {high}")

# Exercise 2: Compare upper vs lower triangle sums : Write a function that calculates the sum of the values ABOVE the main diagonal
# the sum of the values BELOW the main diagonal and returns whichever total is higher.

def trianglesum(matrix):
    uppersum = []
    diagonal = -1
    for x in range(len(matrix)):
        diagonal += 1
        for y in range(len(matrix[0])):
            if y > diagonal:
                uppersum.append(matrix[x][y])
    print("Higher traingle sum:", sum(uppersum))

    lowersum = []
    diagonal = -1
    for x in range(len(matrix)):
        diagonal += 1
        for y in range(len(matrix[0])):
            if y < diagonal:
                lowersum.append(matrix[x][y])
    print("Lower traingle sum:", sum(lowersum))
               
           


# Extra credit : Find the absolute difference between diagonal sums
def diagonal_difference(matrix):
    firstdiagonal = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if y == x:
                firstdiagonal += matrix[x][y]
    print("First Diagonal:",firstdiagonal)

    length = len(matrix[0]) - 1
    seconddiagonal = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if y == x:
                seconddiagonal += matrix[x][length - y]
    print("Second Diagonal:",seconddiagonal)
    absolute = [firstdiagonal, seconddiagonal]
    absolutee = max(absolute)-min(absolute)
    print ("Absolute difference:",absolutee)
