# 004. Pi
# Split the sentence "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics". into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.
s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sList = s.replace(',', '').replace('.', '').split(' ')
numList = []
for i in range(len(sList)):
    numList.append(len(sList[i]))
print(numList)