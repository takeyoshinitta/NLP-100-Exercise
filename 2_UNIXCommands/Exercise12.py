# 12. col1.txt from the first column, col2.txt from the second column
# Extract the value of the first column of each line, and store the output into col1.txt. Extract the value of the second column of each line, and store the output into col2.txt. Confirm the result by using cut command.

firstColumn = []
secondColumn = []
with open('popular-names.txt') as f:
    lines = f.readlines()
    for i in lines:
        lineArray = i.split('\t')
        firstColumn.append(lineArray[0])   
        secondColumn.append(lineArray[1]) 
    f.close()    

with open('col1.txt', 'w') as f:
    for i in range(len(firstColumn)):
        f.write(firstColumn[i] + "\n")
    f.close()

with open('col2.txt', 'w') as f:
    for i in range(len(secondColumn)):
        f.write(secondColumn[i] + "\n")
    f.close()