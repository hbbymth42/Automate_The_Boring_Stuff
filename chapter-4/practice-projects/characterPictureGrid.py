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
rowItem = 0
for rowLine in range(len(grid[rowItem])):
    while rowItem < len(grid):
        print(grid[rowItem][rowLine], end="")
        rowItem += 1
    print("\n")
    rowItem = 0
    