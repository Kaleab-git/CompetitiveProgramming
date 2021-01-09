A = [[1, 3, 4],[2, 2, 3],[1, 2, 4]]
visible = 0
for row in range(3):
    visible += A[row][0]
    for column in range(2):
        if A[row][column] < A[row][column+1]:
            visible += A[row][column+1] - A[row][column]
    visible += A[row][2]
    for column in range(2,0,-1):#going backwards through each row this time. Determining sides as seen from the opposite side
        if A[row][column] < A[row][column-1]:
            visible += A[row][column-1] - A[row][column]

for column in range(3):
    visible += A[0][column]
    for row in range(2):
        if A[row][column] < A[row+1][column]:
            #print ('printing A[column][row] and A[column][row+1]:', A[row][column], 'and', A[row][column])
            visible += A[row+1][column] - A[row][column]
    print (visible)
    visible += A[2][column]
    print ('hi: ', A[2][column])
    for row in range(2,0,-1):#going backwards through each row this time. Determining sides as seen from the opposite side
        print ('row',row)
        if A[row][column] < A[row-1][column]:
            visible += A[row-1][column] - A[row][column]

print (visible + 18)
