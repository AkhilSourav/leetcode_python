def BFS(i, j, visited, grid):
    visited[i][j] = True
    queue = []
    queue.append((i, j))
    n = len(grid)
    m = len(grid[0])
    
    while queue:
        i,j = queue.pop(0)
        # del_row and del_col are used to traverse the 8 neighbours of a node
        for del_row in [-1,0,1]:
            for del_col in [-1,0,1]:
                neigh_row = i + del_row
                neigh_col = j + del_col
                # First check if the neighbour is valid and then check if it is a land and not visited
                if (
                    neigh_row >= 0 and neigh_col >= 0 and neigh_row < n and neigh_col < m and
                    visited[neigh_row][neigh_col] == False and grid[neigh_row][neigh_col] == 1
                   ):
                    queue.append((neigh_row, neigh_col))
                    visited[neigh_row][neigh_col] = True
        

# Given Grid
grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0]
    ]

n = len(grid)
m = len(grid[0])

# Create a visited matrix for the grid
visited = [[False]* m for _ in range(n)]

count = 0

# Traverse the grid
for i in range(n):
    for j in range(m):
        # If the node is not visited and it is a land
        if visited[i][j] == False and grid[i][j] == 1:
            BFS(i, j, visited, grid)
            count += 1

print(f"Number of islands: {count}")