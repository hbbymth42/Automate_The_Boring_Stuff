grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

HEIGHT = len(grid[0]) # Max Height = 6, Max Index = 5
WIDTH = len(grid) # Max Width = 9, Max Index = 8
columnNum = 0
for rowNum in range(len(grid[columnNum])):
    while columnNum < len(grid):
        print(grid[columnNum][rowNum], end="")
        columnNum += 1
    print("\n")
    columnNum = 0
    