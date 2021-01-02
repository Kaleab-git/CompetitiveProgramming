array = [1, 3, 2, 6, 1, 2]
k = 3
n = len(array)
count = 0 

for i in range(n):
    for j in range (i, n):
        sum = array[i] + array[j]
        if (i < j) and (sum%k == 0):
            count += 1

print (count)
