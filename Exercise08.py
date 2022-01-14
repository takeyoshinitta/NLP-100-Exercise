# 08. cipher text
"""
Implement a function cipher that converts a given string with the specification:
    *Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
    *Keep other letters unchanged
Use this function to cipher and decipher an English message.
"""

def cipher(str):
    c = list(str)
    newStr = ''
    for i in range(len(c)):
        if (c[i].isalpha() and c[i].islower()):
            c[i] = chr(219 - ord(c[i]))
        newStr = f'{newStr}{c[i]}'
    print(newStr)

cipher('Hello World!') # print 'Hvool Wliow!'
cipher('Hvool Wliow!') # print 'Hello World!'
