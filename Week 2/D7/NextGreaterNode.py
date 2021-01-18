# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        i = head; j = i.next
        answer = []
        next_greater_node = False
        while i != None:
            while j != None:
                if j.val > i.val:
                    answer.append(j.val)
                    next_greater_node = True
                    break
                j = j.next
            if next_greater_node != True:
                answer.append(0)
            next_greater_node = False
            i = i.next
            j = i    
        return answer