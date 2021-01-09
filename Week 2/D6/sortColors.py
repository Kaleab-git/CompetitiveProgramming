A = [2,0,1,2,1,0,2,1,0]

def sortColors(A):
    zI = 0; tI = len(A) -1
    print (A)
    for i in range(len(A)):
        if A[i] == 0:
            A[i], A[zI] = A[zI], A[i]
            zI += 1
        elif A[i] == 2:
            A[i], A[tI] = A[tI], A[i]
            tI -= 1
        print (A)
    return A
print (sortColors(A))