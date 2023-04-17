def DFS(x, y, prev, target, del_row, del_col, visited, grid):
    visited[x][y] = True
    
    # Traverse the 4 neighbours of the node
    for i in range(4):
        new_x = x + del_row[i]
        new_y = y + del_col[i]
        if ( new_x >=0 and new_y >=0 and new_x < len(grid) and new_y < len(grid[0]) and
             visited[new_x][new_y] == False and grid[new_x][new_y] == prev
            ):
            grid[new_x][new_y] = target
            DFS(new_x, new_y, prev, target, del_row, del_col, visited, grid)

            
def flood_fill_algo(grid):
    n = len(grid)
    m = len(grid[0])

    # Create a visited matrix for the grid
    visited = [[False]* m for _ in range(n)]

    # Coordinates of the starting node
    x , y = 4, 4
    
    # Current color to be replaced
    prev = grid[x][y]

    # final color
    target = 3

    # del_row and del_col are used to traverse the 4 neighbours of a node
    del_row = [0 , -1 , 0 , 1]
    del_col = [-1 , 0 , 1 , 0]

    grid[x][y] = target
    
    # Call DFS
    DFS(x, y, prev, target, del_row, del_col, visited, grid)

    # Print the grid after flood fill
    for row in grid:
        print(row)


# Given Grid
grid = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]
    
flood_fill_algo(grid)