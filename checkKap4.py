grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def possible(y,x,n):
    global grid
    for i in range (0,9):
        checker = grid[y][i]
        if checker == n:
            return False
    for i in range (0,9):
        if grid[i][x] == n:
            return False
    return True

print(possible(1, 0, 7))


