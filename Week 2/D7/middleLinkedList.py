class Solution(object):
    def get_size(self, head):
        node = head
        size = 0
        while node != None:
            size+=1
            node = node.next
        return size
    def middleNode(self, head):
        node = head
        middle = self.get_size(head)//2
        current_index = 0
        while current_index != middle:
            node = node.next
            current_index += 1
        return node