tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data)
    count = 0

    while count < len(data):
        for item in data[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1

    for word in range(len(data[0])):
        for item in range(len(data)):
            print(data[item][word].rjust(colWidths[item]), end=' ')
        print()
        
printTable(tableData)