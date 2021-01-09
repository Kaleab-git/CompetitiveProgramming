def countingSort(A):
    Max = A[0]
    counterList = []
    for i in A:
        if i > Max:
            Max = i
    for i in range(Max+1):
        counterList.append(0)
    for i in range(len(A)):
        counterList[A[i]] += 1
    A.clear()
    for i in range(Max+1):
        for j in range(counterList[i]):
            A.append(i)
    return A

def findMedian(arr):
    arr = countingSort(arr)
    median = arr[len(arr)//2]
    return median
arr = [0,1,2,4,6,5,3]
print (findMedian(arr))