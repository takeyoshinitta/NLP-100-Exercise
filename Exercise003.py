# 003. "shoe" + "cold" = "schooled"
# Obtain the string "schooled" by concatenating the letters in "shoe" and "cold" one after the other from head to tail.
s1 = 'shoe'
s2 = 'cold'
s1List = list(s1)
s2List = list(s2)
newStr = ''
for i in range(0, 4):
    newStr += s1List[i] + s2List[i]
print(newStr)
