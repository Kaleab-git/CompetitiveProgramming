# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        i = head; j = head
        answer = []
        while i != None:
            local_max = i.val
            while j != None:
                if j.val > local_max:
                    local_max = j.val
                    break
                j = j.next
            if local_max == i.val:
                answer.append(0)
            else:
                answer.append(local_max)
            i = i.next
            j = i        
        return answer