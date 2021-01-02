ru = 'a' #repeatingUnit
string = ''
n = 101000000000000
si = 0 # string index

def repeatedString(s, n):
    string = ''
    si = 0
    count = 0
    if len(s) == 1:
        return n
    while len(string) != n:
       string += ru[si]
       if si == len(ru)-1:
           si = 0
       else:
          si += 1
    for i in string:
        if i == 'a':
            count+= 1
    print (string)
    return count

print (repeatedString('a', 1000000000000))