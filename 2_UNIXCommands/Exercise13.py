# 13. Merging col1.txt and col2.txt
# Join the contents of col1.txt and col2.txt, and create a text file whose each line contains the values of the first and second columns (separated by tab character) of the original file. Confirm the result by using paste command.

mergedColumn = []
with open('col1.txt') as f1:
    with open('col2.txt') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(len(lines1)):
            mergedColumn.append(lines1[i].rstrip() + '\t' +  lines2[i])
        f2.close()
    f1.close()

with open('merged.txt', 'w') as f:
    for i in range(len(mergedColumn)):
        f.write(mergedColumn[i])
    f.close()
