def selectionSort(A):
    l = len(A)
    for i in range(l):
        Min  = A[i]
        index = i
        for j in range(i, l):
            if Min > A[j]:
                Min = A[j]
                index = j
        A[i], A[index] = A[index], A[i]
    return A

A = [4,3,6,2,6,1]
print (selectionSort(A))