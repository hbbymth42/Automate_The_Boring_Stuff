def printTable(table):
    colWidths = [0] * len(table)
    # Find Max Length for each column
    for i in range(len(table)):
        longWord = table[i][0]
        for j in range(len(table[i])):
            if len(longWord) < len(table[i][j]):
                longWord = table[i][j]
        colWidths[i] = len(longWord)
    columnNum = 0
    for rowNum in range(len(table[columnNum])):
        while columnNum < len(table):
            print(table[columnNum][rowNum].rjust(colWidths[columnNum]), end=" ")
            columnNum += 1
        print("\n")
        columnNum = 0


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)