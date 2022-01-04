# 01. Reversed String
# Obtain the string that arranges letters of the string "stressed" in reverse order (tail to head) 
str = 'stressed'
strList = list(str)
newStr = ''
for i in range(len(strList), 0, -1):
    newStr += strList[i-1]
print(newStr)
