class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = 0 
        # rearrange all dominoes to ensure dominoe[i][0] <= dominoe[i][1]
        for dominoe in dominoes: 
            if dominoe[0] > dominoe[1]:
                dominoe[0], dominoe[1] = dominoe[1], dominoe[0]
        #sort dominoes by first element
        dominoes.sort()
        print (dominoes)
        temp = []
        anotherCount = 0
        for i in range(len(dominoes)-1):
            if self.checkEquivalence(dominoes[i], dominoes[i+1]):
                count += 1
                if not temp:
                    temp = dominoes[i]
                else:
                    count += anotherCount + 1
                    anotherCount += 1
            else:
                anotherCount = 0
                temp = []
        return count
    
    def checkEquivalence(self, arr1, arr2):
        if arr1[0] == arr2[0] and arr1[1] == arr2[1]:
            return True
        elif arr1[0] == arr2[1] and arr1[1] == arr2[0]:# not needed
            return True
        return False