# 18. Sort lines in descending order of the third column
# Sort the lines in descending numeric order of the third column (sort lines without changing the content of each line). Confirm the result by using sort command.

def insertion(A, id):
    for j in range(1,len(A)):
        key = A[j]
        keyID = id[j]
        i = j - 1
        while (i >= 0 and id[i] > keyID):
            A[i + 1] = A[i]
            id[i + 1] = id[i]
            i = i - 1
        A[i + 1] = key
        id[i + 1] = keyID
    return A

with open('popular-names.txt') as f:
    thirdColumn = []
    lines = f.readlines()
    for i in lines:
        lineArray = i.split('\t')
        thirdColumn.append(int(lineArray[2]))
    sortedList = insertion(lines, thirdColumn)
    f.close()
    with open('sorted.txt', 'w') as fw:
        for i in range(len(sortedList)):
            fw.write(sortedList[i])
        fw.close()
