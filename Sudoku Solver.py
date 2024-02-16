#  sudoku is 9*9 grid puzzle where each cell can contain a number from 1 to 9 
# To win we must fill all the cells in a way that same number is not repaeated in a same row or coloumn or the same subgrid  
# In each row coloumn or subgrid , each number must be unique
#We are using a techinique called backtracking we keep trying different possibilities untilwe find a valid solution 

def is_valid(grid, r, c, k):

    not_in_row = k not in grid[r]  #k not in row

    not_in_column = k not in [grid[i][c] for i in range(9)] #k not in row

    not_in_box = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)] # k not in the subgrid 

    return not_in_row and not_in_column and not_in_box 


def solve(grid, r=0, c=0):
    if r == 9: #if row 9 the solved
        return True
    elif c == 9: # if coloumn 9 we have to move next row
        return solve(grid, r+1, 0)
    elif grid[r][c] != 0: # if the coloumn is alreadey filled move to next
        return solve(grid, r, c+1)
    else:
        for k in range(1, 10): #filling the numbers by using recursion and backtracking 
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                if solve(grid, r, c+1):
                    return True
                grid[r][c] = 0 #if not matched make the value zero again
        return False
        
    
# We can represent the grid with a 9*9 matrix of integers where a cell can have a value from 1 to 9 or 0 if its empty     
grid = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
]
solve(grid)
if solve(grid)==True :
 
 print(*grid, sep='\n')

else: 
    print("NO possibility")



# Recursion is a process in which a function calls itself directly or indirectly.
# Backtracking is an algorithmic technique that builds a solution incrementally, one piece at a time, while eliminating choices that fail to satisfy problem constraints