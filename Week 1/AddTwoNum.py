# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# l1 is [2,4,3] and l2 is [5,6,4]

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        print ('hi')
        #n1 = l1.val
        #n2 = l2.val
        #while n1.value:
         #   n1 = n1.val + n1
    
l1 = [2,4,3]

for i in range(len(l1)-1):
    ListNode(l1[i], l1[i+1])


sol = Solution()

sol.addTwoNumbers(l1, [5,6,4])
        
