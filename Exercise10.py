# 10. Line count
# Count the number of lines of the file. Confirm the result by using wc command.

count = 0
with open('popular-names.txt') as f:
    for line in f:
        count += 1
print ('Number of lines is ' + str(count))