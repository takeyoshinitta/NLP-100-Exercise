# 01. "schooled"
# Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string "schooled".
str = 'schooled'
strList = list(str)
newStr = ''
for i in range(1, len(strList), 2):
    newStr += strList[i]
print(newStr)
