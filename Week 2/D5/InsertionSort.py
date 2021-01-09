def insertionSort(A):
    length = len(A)
    for i in range(length):
        ix = i
        for j in range(i, -1, -1):
            print (A[ix], A[j])
            if A[ix] < A[j]:
                A[ix], A[j] = A[j], A[ix]
                ix -= 1
        print (A)
    return A

A = [4,3,6,2,1,6]
print (insertionSort(A))


