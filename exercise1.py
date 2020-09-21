
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    col_widths = [0] * len(table)
    
    for y in range(len(table)):
        for x in table[y]:
            if col_widths[y] < len(x):
                col_widths[y] = len(x)

    for x in range(len(table[0])) :
        for y in range(len(table)) :
            print(table[y][x].ljust(col_widths[y]), end = ' ')
        print()
        x += 1

print_table(tableData)