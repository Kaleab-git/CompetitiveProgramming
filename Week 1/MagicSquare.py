magicSquarePermutations = [[[8,3,4], [1,5,9], [6,7,2]], [[8,1,6], [3,5,7], [4,9,2]], [[6,1,8], [7,5,3], [2,9,4]], [[4,9,2], [3,5,7], [8,1,6]], [[2,9,4], [7,5,3], [6,1,8]], [[4,3,8], [9,5,1], [2,7,6]], [[6,7,2], [1,5,9], [8,3,4]], [[2,7,6], [9,5,1], [4,3,8]]]

def formingMagicSquare(s):
    cost = 0 #variable to store runnig sum of costs of switching each element
    minCost = 45 #initialize minCost to the largest possible Cots we could get so that for the first comparison of a matric it will always be greater than cost.
#the greatest cost is if we're given a 0x0 matrix as input. In this case the cost of converting to any one permutation of the magicSquare will always be 45
    for i in magicSquarePermutations:#i is a magicSquare
        for j in range(3):# j is 1 row of that magicSquare
            for k in range(3):# k is an item in that row
                cost += abs(i[j][k] - int(s[j][k]))
        if minCost >= cost:
            minCost = cost
        cost = 0
    return minCost

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

print (formingMagicSquare(s))