import math, collections
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers); total = count[0]
        for color in count:
            if color != 0: total += (color*math.ceil(count[color]/(color+1))) + math.ceil(count[color]/(color+1))
        return total                
        
        
