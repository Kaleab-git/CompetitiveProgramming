# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def listItems(self, head):
        node = head
        list_of_nodes = []
        while node != None:
            list_of_nodes.append(node.val)
            node = node.next
        list_of_nodes.reverse()
        return list_of_nodes
    
    def reverseList(self, head):
        node = head
        list_of_nodes = self.listItems(head)
        print (list_of_nodes)
        for i in list_of_nodes:
            print (node.val)
            node.val = i
            print (node.val)
            node = node.next
        return head