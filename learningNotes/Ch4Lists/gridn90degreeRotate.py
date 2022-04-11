grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(grid)
# print(len(grid[:]))
# print(len(grid[0][:]))
width=len(grid[:])
height=len(grid[0][:])
new_grid = []
print(range(height))

for x in range(height):
        for y in range(width):
                print(grid[y][x], end='')
        print()                