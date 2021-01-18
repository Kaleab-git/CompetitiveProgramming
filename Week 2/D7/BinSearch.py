A = [8,9,10,11,12,13,14,15]
#doesn't work for the first index
def binSearch(A,k,index=len(A)//2):
    n = len(A)
    if A[n//2] == k:
        return index
    elif A[n//2] > k:
        index -= n//4
        return binSearch(A[:n//2],k,index)
    elif A[n//2] < k:
        index += n//4
        return binSearch(A[n//2:],k,index)
    else:
        return -1

print  (binSearch(A,8))