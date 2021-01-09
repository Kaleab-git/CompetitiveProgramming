def bubbleSort(A):
    for j in range(len(A)):
        for i in range(len(A)-1):
          if A[i] > A[i+1]:
              A[i], A[i+1] = A[i+1], A[i]
    return A

A = [4,3,6,2,1,6]

print (bubbleSort(A))