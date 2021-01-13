class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def addAtHead(self, val):
        #a far better approach would be head = Node(value, head) and thats it. No more line of code.
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
        if self.get_size() == 0:
            self.addAtHead(val)
        else:
            while node.next != None:
                node = node.next
            node.next = Node(val)
    def addAtIndex(self, index, val):
        if index == 0: #to get an O(1) if we're to add at head
            self.addAtHead(val)
        elif index == self.get_size():#to divide tasks between functions
            self.addAtTail(val)
        elif index < self.get_size():
            new_node = Node(val)
            node = self.head
            current_index = 0
            while current_index+1 < index:
                node = node.next
                current_index += 1
            new_node.next = node.next
            node.next = new_node
    def deleteAtIndex(self, index):
        node = self.head
        size = self.get_size()
        current_index = 0
        if size == 0 or size <= index:
            return
        elif size == 1 and index == 0:
            self.head = None
            return
        while current_index+1 < index:
            current_index += 1
            node = node.next
        if index == 0:
            self.head = node.
            return 
        elif node.next.next == None:
            node.next = None
        else:
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