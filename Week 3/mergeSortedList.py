# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        i = l1; j = l2
        head = ListNode()
        temp = head
        while i!=None or j!=None:
            if i == None and j != None:
                temp.next = ListNode(j.val)
                j = j.next
            elif i != None and j == None:
                temp.next = ListNode(i.val)
                i = i.next
            else:
                if i.val < j.val:
                    temp.next = ListNode(i.val)
                    if i != None:
                        i = i.next
                else:
                    temp.next = ListNode(j.val)
                    if j != None:
                        j = j.next
            temp = temp.next
                
                            
        return head.next


#Doesnt work

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        i =  l1; j = l2 
        head = ListNode()
        while i != None or j != None:
            if i == None and j != None:
                if head.val = 0:
                    head = ListNode(j.val)
                    temp = ListNode()
                else:
                    answer.next = ListNode(j.val)
                    answer = answer.next
                    j = j.next
            elif i != None and j == None:
                answer.next = ListNode(i.val)
                answer = answer.next
                i = i.next
            elif i.val < j.val:
                answer.next = ListNode(i.val)
                answer = answer.next
                i = i.next
            else:
                answer.next = ListNode(j.val)
                answer = answer.next
                j = j.next
        return answer
"""