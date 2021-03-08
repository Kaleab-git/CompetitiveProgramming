# 123 ~ 321.  -123 ~ -321. 120 ~ 21. 0 ~ 0
# range [-2^31, 2^31-1]

def reverse(x):
    string = str(x)
    signed = False
    if x == 0:
        return 0
    if '-' in string:
        string = string[1:]
        signed = True
    # remove all zeros.
    while string[-1] == '0':
        string = string[:-1]
    # now reverse it and add sign if it was negative.
    reversedNum = string[::-1]
    if signed == True:
        reversedNum = '-' + reversedNum
    if int(reversedNum) > (2**31 - 1) or int(reversedNum) < (0-2**31):
        return 0
    else:
        return int(reversedNum)
