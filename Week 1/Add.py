def reverseString(string):
    return string[::-1]
#correcting unequal length here
def correctLength(n1, n2):
    if len(n1) < len(n2):
        diff = len(n2) - len(n1)
        n1 = ('0'*diff) + n1
    else:
        diff = len(n1) - len(n2)
        n2 = ('0'*diff) + n2
    return n1, n2

def Add(n1, n2):
    result = ''; carry = 0
    n1, n2 = correctLength(n1, n2)
    n1 = reverseString (n1); n2 = reverseString (n2)
    for i in range(len(n1)):
        if int(n1[i]) + int(n2[i]) + carry <= 9:
            result += str(int(n1[i]) + int(n2[i]) + carry)
            carry = 0
        elif (int(n1[i]) + int(n2[i]) + carry > 9) and (i!=len(n1)-1):
            result += str ((int(n1[i]) + int(n2[i]) + carry)%10)
            carry = 1
        else:
            result += reverseString(str(int(n1[i]) + int(n2[i]) + carry))
    return reverseString(result)

n1 = input ('First number: ')
n2 = input ('Second number: ')



print (Add(n1, n2))
