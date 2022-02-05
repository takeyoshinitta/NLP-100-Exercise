# 16. Split a file into N pieces
# Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries. Confirm the result by using split command.
from sys import argv

if (len(argv) > 1 & argv[1].isdigit()):
    n = int(argv[1])
    with open('popular-names.txt') as f:
        lines = f.readlines()
        lineNum = len(lines)
        outLinesNum = lineNum / n
        i = 0
        for j in range(n):
            with open(f'split{j}.txt', 'w') as wf:
                for k in range(int(outLinesNum)):
                    wf.write(lines[i])
                    i = i + 1
                wf.close()
        f.close()

else:
    print("type appropriate number")