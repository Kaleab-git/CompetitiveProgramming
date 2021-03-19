class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights); r = sum(weights)
        working_capacity = r
        while l <= r:
            capacity = (r+l)//2
            days = self.verifyCapacity(capacity, D, weights)
            if days > D:#means I'm allowing too much. Decrease capacity
                l = capacity+1
            else:#means I'm allowing too little. Increase capacity
                r = capacity-1
        return l
                
    def verifyCapacity(self, capacity, D, weights):
        days = 0; Sum = 0
        for i in range(len(weights)):
            if Sum + weights[i] > capacity:
                Sum = 0; days += 1
            Sum += weights[i]
        days += 1
        return days