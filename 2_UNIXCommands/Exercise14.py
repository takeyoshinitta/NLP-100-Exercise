# 14. First N lines
# Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. Confirm the result by using head command.
from sys import argv

n = 0;
if (len(argv) > 1 & argv[1].isdigit()):
    n = argv[1]
    with open('popular-names.txt') as f:
        line = f.readlines()
        for i in range(0, int(n)):
            print(line[i].rstrip())
        f.close()

else:
    print("type appropriate number")