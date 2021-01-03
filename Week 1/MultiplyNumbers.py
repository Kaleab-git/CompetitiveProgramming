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
    
def multiply(n1, n2):
    r = ''; rList = []; carry = 0; addZeros = 0; result = 0#r to store each semi-product. #addZeros to handle the left shit.
    n1 = reverseString (n1); n2 = reverseString (n2)
    for k,i in enumerate(n1):
        for l,j in enumerate(n2):
            i = int(i); j = int(j)
            if  i*j + carry <= 9:    
                r += str ((i * j) + carry)
                carry = 0
            elif (i*j) + carry > 9 and (l != len(n2)-1): #(l != len(n2)-1) to make sure we're not at the end of our string 
                r += str(((i*j) + carry)%10)
                carry = ((i*j)+carry)//10
            else:
                r += reverseString(str((i*j) + carry))
                carry = 0 #resetting carry to calculate the next semi-product

        r = '0'*addZeros + r
        rList.append(reverseString(r))
        r = '' 
        addZeros += 1
    #adding all semi-products
    for i in range(len(rList)):
        result = Add(str(result), str(rList[i]))
    return result

n1 = input('Number 1: ')
n2 = input('Number 2: ')

print (multiply(n1, n2))
