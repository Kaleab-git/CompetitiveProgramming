A = [2,0,2,2,7,9]
# counter = [0,0,0,0,0,0,0]
def countingSort(A):
    Max = A[0]
    counterList = []
    #Loop to search for Maximum number
    for i in A:
        if i > Max:
            Max = i
    #Loop to initializw counterList with length = 100 and with each element equal to 0
    for i in range(Max+1):
        counterList.append(0)
    #loop to count appearance of each element
    for i in range(len(A)):
        counterList[A[i]] += 1
    A.clear()
    for i in range(Max+1):
        for j in range(counterList[i]):
            A.append(i)
    return A
    


print (countingSort(A))
