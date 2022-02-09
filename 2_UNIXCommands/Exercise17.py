# 17. Distinct strings in the first column
# Find distinct strings (a set of strings) of the first column of the file. Confirm the result by using cut, sort, and uniq commands.

def removeDuplicates(list):
    newList = []
    for i in list:
        if not(i in newList):
            newList.append(i)
    return newList

with open('popular-names.txt') as f:
    firstColumn = []
    lines = f.readlines()
    for i in lines:
        lineArray = i.split('\t')
        firstColumn.append(lineArray[0])
    size = len(removeDuplicates(firstColumn))
    print(f'There are {size} set of strings')
    f.close