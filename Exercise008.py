# 008. Template-based sentence generation
# Implement a function that receives arguments, x, y, and z and returns a string "{y} is {z} at {x}", where "{x}", "{y}", and "{z}" denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.

def tempSentence(x, y, z):
    return f'{y} is {z} at {x}'

x = 12
y = 'temperature'
z = 22.4

print(tempSentence(x, y, z))