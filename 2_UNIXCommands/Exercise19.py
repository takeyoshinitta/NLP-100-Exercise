# 19. Frequency of a string in the first column in descending order
# Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies. Confirm the result by using cut, uniq, and sort commands.

import collections as c

with open('popular-names.txt') as f:
    firstColmn = []
    lines = f.readlines()
    for i in lines:
        lineArray = i.split('\t')
        firstColmn.append(lineArray[0])
        
    frequencyList = c.Counter(firstColmn)

    with open('frequency-names.txt', 'w') as fw:
        for i in frequencyList.most_common():
            fw.write(i[0] + '\n')