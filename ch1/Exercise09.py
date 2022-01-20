# 09. Typoglycemia
"""
Write a program with the specification:

    *Receive a word sequence separated by space
    *For each word in the sequence:
        *If the word is no longer than four letters, keep the word unchanged
        *Otherwise,
            *Keep the first and last letters unchanged
            *Shuffle other letters in other positions (in the middle of the word)

Observe the result by giving a sentence, e.g., "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
"""
import random

def typoglycemia(str):
    strList = str.split(' ')
    if (len(strList) <= 4):
        print(str)
    else:
        middleWordsList = strList[1:-1]
        randomStr = ' '.join(random.sample(middleWordsList, len(middleWordsList)))
        print(f'{strList[0]} {randomStr} {strList[-1]}')

typoglycemia('I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind.')
