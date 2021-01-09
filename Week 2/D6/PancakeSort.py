class Solution:
    def pancakeSort(self, arr):
        steps = []
        for n in range(len(arr), 0, -1):              
            steps.extend([arr.index(n) + 1, n])  
            arr = arr[:arr.index(n):-1] + arr[:arr.index(n)]     
        return steps
            