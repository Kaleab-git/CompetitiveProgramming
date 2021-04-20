class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==0: return sum(x for x in range(1,n,2))
        return sum(x for x in range(2,n,2))
"""
if n=odd, then we wanna bring all the numbers to middle one. 
And its going to cost the middle element 0 to do that.
Its going to cost the immediate neighbors 2. Then 4. Then 6.....
Since the cost of adding and substrating together is one. We only need to worry about one half of the array
For n=7 for example, 7//2=3. We have 3 numbers on each side of the middle element. And its going to cost
2, 4, 6 respecitively for each. 
So for n%2!=0, cost=sum(x for x in range(2,n,2)).
-------------------------------And it works. Can you believe that? It works. Yeay math---------------------------------
"""
"""
Now for even numbers. Since we have 2 numbers as our middle, we move all numbers to their average. 
For n=6, [1,3,5,7,9,11] we wannna change all the numbers to (5+7)//2, which not coincedentally=n 
Again we only have to conern ourselves with one half of the array. The cost to change 1,3,5 to 6 is 
5+3+1.
So for n%2==0, cost=sum(x for x in range(1,n,2))
