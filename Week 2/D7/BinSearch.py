A = [8,9,10,11,12,13,14,15]
#doesn't work for the first index
def bin_search(A,k,index=len(A)//2):
    n = len(A)
    if A[n//2] == k:
        return index
    elif A[n//2] > k:
        index -= n//4
        return bin_search(A[:n//2],k,index)
    elif A[n//2] < k:
        index += n//4
        return bin_search(A[n//2:],k,index)
    else:
        return -1
#works fine
def binary_search(A, lo, hi, k): 
    if hi >= lo: 
        mid = (hi + lo) // 2
        if arr[mid] == k: 
            return mid 
        elif arr[mid] > k: 
            return binary_search(arr, lo, mid - 1, k)  
        else: 
            return binary_search(arr, mid + 1, hi, k) 
    else: 
        return -1
arr = [8,9,10,11,12,13,14,15]
x = 15
result = binary_search(arr, 0, len(arr)-1, x) 
print (result)