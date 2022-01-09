# 006. n-gram
# Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence "I am an NLPer"

def n_gram(n, list):
    newList = []
    for i in range(n - 1):
        if(list[i] + ', ' + list[i+1] in newList):
            continue
        else:
            newList.append(list[i] + ', ' + list[i+1])
    return newList

s = 'I am an NLPer'

sList = s.split(' ')
print('Word Bi-gram: ' + str(n_gram(len(sList), sList)))

sList = list(s)
print('Letter Bi-gram: ' + str(n_gram(len(sList), sList)))