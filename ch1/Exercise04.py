# 04. Atomic symbols
#Split the sentence "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can". into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words. Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
sList = s.split(' ')
newList = {}
for i in range(1, len(sList) + 1):
    if (i in [1, 5, 6, 7, 8, 9, 15, 16, 19]):
        newList[sList[i-1][:1]] = i
    else:
        newList[sList[i-1][:2]] = i
print(newList)
