class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0; bought = False; increasing = False
        
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]: increasing = True
            elif prices[i] > prices[i+1]: increasing = False
            
            if bought and not increasing:#sell @ i
                bought = False; profit += prices[i]
            elif not bought and increasing:#buy @ i
                bought = True; profit -= prices[i]
        
        if bought: profit += prices[-1]
            
        return profit