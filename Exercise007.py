# 007. Set
# Let the sets of letter bi-grams from the words "paraparaparadise" and "paragraph" X and Y, respectively. Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram "se" is included in the sets X and Y

def bi_gram(n, list):
    newList = []
    for i in range(n-1):
        if('(' + list[i] + ', ' + list[i+1] + ')' in newList):
            continue
        else:
            newList.append('(' + list[i] + ', ' + list[i+1] + ')')
    return newList

def union(listA, listB):
    newList = []
    for i in range(len(listA)):
        newList.append(listA[i])
    for i in range(len(listB)):
        if (listB[i] in newList):
            continue
        else:
            newList.append(listB[i])
    return newList

def difference(listA, listB):
    newList = []
    for i in range(len(listA)):
        if (listA[i] in listB):
            continue
        else:
            newList.append(listA[i])
    for i in range(len(listB)):
        if (listB[i] in listA):
            continue
        else:
            newList.append(listB[i])
    return newList

def intersection(listA, listB):
    newList = []
    for i in range(len(listA)):
        if (listA[i] in listB):
            newList.append(listA[i])
    return newList

def check_bi_gram(list):
    check = False
    bi_gram = '(s, e)'
    if (bi_gram in list):
        check = True
    return check

def makeSet(list):
    s = str(list).replace('[', '{').replace(']','}').replace("'", '')
    return s

s1 = 'paraparaparadise'
s2 = 'paragraph'

letterList1 = list(s1)
letterList2 = list(s2)

X = bi_gram(len(letterList1), letterList1)
Y = bi_gram(len(letterList2), letterList2)
print('X: ' + makeSet(X))
print('Y: ' + makeSet(Y))
print('X union Y: ')
print(makeSet(union(X, Y)))
print('X difference Y: ')
print(makeSet(difference(X, Y)))
print('X intersection Y: ')
print(makeSet(intersection(X, Y)))

print ('')

if (check_bi_gram(X)):
    print('the bi-gram "se" is included in the sets X')
else:
    print('the bi-gram "se" is NOT included in the sets X')
if (check_bi_gram(Y)):
    print('the bi-gram "se" is included in the sets Y')
else:
    print('the bi-gram "se" is NOT included in the sets Y')