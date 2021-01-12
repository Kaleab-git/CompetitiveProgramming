class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addAtHead(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
    def get(self, index): 
        node = self.head
        current_index = 0
        while node != None:
            if current_index == index:
                return node.val
            else:
                current_index += 1
                node = node.next
        return -1
    def addAtTail(self, val):
        node = self.head
        while node.next != None:
            node = node.next
        node.next = Node(val)
    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index == self.get_size():
            self.addAtTail(val)
        elif index < self.get_size():
            new_node = Node(val)
            node = self.head
            current_index = 0
            while current_index+1 < index:
                node = node.next
                current_index += 1
            #print ('new_node',new_node.val, 'node', node.val, 'node.next', node.next.val)
            new_node.next = node.next
            node.next = new_node
    def deleteAtIndex(self, index):
        node = self.head
        current_index = 0
        if self.get_size == 1:
            self.head = None
        elif self.get_size != 0:
            while current_index+1 < index:
                print ('I deleted stuff')
                node = node.next
                current_index += 1
            node.next = node.next.next 

    def get_size(self):
        node = self.head
        size = 0
        while node != None:
            size+=1
            node = node.next
        return size

    def print_nodes(self):
        node = self.head
        while node != None:
            print (node.val, ' ', end='')
            node = node.next        
        print ()
l = LinkedList()
l.addAtHead(1)
l.addAtTail(3)
l.print_nodes()
l.addAtIndex(1,2)
l.print_nodes()
print ()
print (l.get(1))
l.deleteAtIndex(1)
l.print_nodes()
print ()
print(l.get(1))
