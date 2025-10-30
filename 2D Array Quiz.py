# --------------------------------------------
# Python 2D Arrays Assessment
# Complete each function according to the task.
# --------------------------------------------
mat = [
    [12, 45, 78, 91],
    [23, 56, 84, 99],
    [34, 67, 81, 73],
    [48, 59, 62, 88]
]


# 1️Count all elements in a 2D array

def count_elements(mat):
    elementcount = 0
    for x in mat:
        for y in x:
            elementcount += 1
    print(elementcount, "elements")
    
    # TODO: return how many elements are in the matrix
    


# 2️Return total sum of all elements and subtotal for each row

def sum_elements(mat):
    total = []
    for x in mat:
        rowsum = sum(x)
        index = mat.index(x)
        print(f"Row {index}'s sum: {rowsum}")
        total.append(rowsum)
    
    
    
    
    # TODO: return total sum and a list of row subtotals
    


# 3️Add 1 only to elements on the diagonals

def add_one_diagonal(mat):
    diagonalindex = 0
    for x in mat:
        x[diagonalindex] += 1
        diagonalindex += 1
    for x in mat:
        print(x)
        
    # TODO: return the modified matrix
    


# 4️Swap elements across the main diagonal ( assume array or matrix is square)

def swap_diagonals(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if x<y:
                temp = mat[x][y]
                mat[x][y] = mat[y][x]
                mat[y][x] = temp
    for x in mat:
        print(x)

                
                
                
                
        
    
    # TODO: return the modified matrix

