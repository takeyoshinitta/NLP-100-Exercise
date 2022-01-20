# 11. Replace tabs into spaces
# Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.

with open('popular-names.txt') as f:
    for line in f:
        print(line.strip().replace("\t", " "))