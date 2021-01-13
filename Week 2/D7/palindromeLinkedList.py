# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        node_list = []
        node = head
        while node!=None:
            node_list.append(node.val)
            node = node.next
        if len(node_list) == 0 or len(node_list) == 1:
            return True
        elif node_list == list(reversed(node_list)):
            return True
        else:
            return False