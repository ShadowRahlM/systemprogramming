#! /usr/bin/env python13.3

def printTable(tableData):
    # Initialize colWidths with 0s
    colWidths = [0] * len(tableData)

    # Find the maximum width of each column
    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    # Print each row of the table
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()

# Example usage
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

