# 15. Last N lines
# Receive a natural number $N$ from a command-line argument, and output the last $N$ lines of the file. Confirm the result by using tail command
from sys import argv

n = 0;
if (len(argv) > 1 and argv[1].isdigit()):
    n = int(argv[1])
    with open('popular-names.txt') as f:
        line = f.readlines()
        for i in range(len(line)-1, len(line)-n-1, -1):
            print(line[i].rstrip())
        f.close()

else:
    print("type appropriate number")