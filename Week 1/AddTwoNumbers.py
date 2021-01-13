# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = ''; n2 = ''
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next
        n1 = n1[::-1]
        n2 = n2[::-1]
        result_string = str(int(n1) + int(n2))
        result_string = result_string[::-1]
        head = result = ListNode(int(result_string[0]))
        print (result_string)
        for i in range(1, len(result_string)):
            result.next = ListNode(int(result_string[i]))
            result = result.next
        return head