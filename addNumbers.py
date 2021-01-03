def reverseString(string):
    return string[::-1]

#take input
num1 = input ('First number: ')
num2 = input ('Second number: ')


#Based on the fact that 123 = 100 + 20 + 3 = 1(100) + 2(10) + 3(1)
def addNumbers(num1, num2):
    num1 = reverseString (num1)
    num2 = reverseString (num2)
    firstNum = []
    secondNum = []

    for i in range(len(num1)):
        ithPlace = int(num1[i] + '0'*i)
        firstNum.append(ithPlace)
    for j in range(len(num2)):
        jthPlace = int(num2[j] + '0'*j)
        secondNum.append(jthPlace)
    return (sum(firstNum) + sum(secondNum))

#Based on the fact that 123*456 = (6*30) + (6*20) + (6*100)  +  (40*3) + (40*20) + (40*100)  +  (300*3) + (300*20) + (300*100)
def multiplyNumbers(num1, num2):
    num1 = reverseString (num1); num2 = reverseString (num2)
    firstNum = []; secondNum = []; result = 0

    for i in range(len(num1)):
        ithPlace = int(num1[i] + '0'*i)
        firstNum.append(ithPlace)
    for j in range(len(num2)):
        jthPlace = int(num2[j] + '0'*j)
        secondNum.append(jthPlace)
    #the multiplying part-by-part part
    for i in firstNum:
        for j in secondNum:
            result = addNumbers(str(result), str(i * j)) #str() cause our function expects strings


    return (result)

print (multiplyNumbers(num1, num2))
print (addNumbers(num1, num2))