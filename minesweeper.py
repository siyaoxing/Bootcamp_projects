
input_grid = [["-","-","-","#","#",],
        ["-","#","-","-","-",],
        ["-","-","#","-","-",],
        ["-","#","-","#","-",],
        ["-","#","-","#","-",],
        ["-","#","#","#","#",],
]

#Function to calculate the number of mines around each position in the list, with 3 parameters
def calculate_mines(grid, row, column):
    #return "#" if value in the grid is a mine 
    if grid[row][column] == "#":
        return "#"
    #variable to store mine count
    mine_counter = 0
    #nested for loop to check surrounding 8 values, using row and column co-ordinates
    #returns total number of mines around each position in the grid
    for near_row in range(row-1, row+2):
        for near_column in range(column-1, column+2):
            #if the position been checked is at index row, column: this is the current location so continue 
            if near_row == row and near_column == column:
                continue 
            #if the position been checked is out of range at the top or bottom of the grid, continue 
            if near_row < 0 or near_row >= len(grid):
                continue 
            #if the position been checked is out of range at the left/right of the grid, continue 
            if near_column < 0 or near_column >= len(grid[0]):
                continue 
            #if the position being checked is a mine, +1 to mine counter
            if grid[near_row][near_column] == "#":
                mine_counter +=1
            #print(f"near row: {near_row}, near column: {near_column}")
    return str(mine_counter)



#Function to return a new grid, using values calculated from above function calculate_mines 
def mine_detector (grid):
    #Variable storing length and width of grid
    num_of_rows = len(grid) 
    num_of_columns = len(grid[0])
    #Variable to store new grid with calculated values 
    new_grid = []
    #Nested for loop, iterating through each row and column 
    #Calls function calculate mines for each iteration to return a number, which is appended to new_row
    for row in range(num_of_rows):
        new_row = []
        for column in range(num_of_columns):
            new_row += calculate_mines(grid, row, column)
        new_grid.append(new_row)
    return new_grid

#Print new grid by passing input_grid into the min_detector function 
[print(mine_detector(input_grid)[x]) for x in range(len(input_grid))]