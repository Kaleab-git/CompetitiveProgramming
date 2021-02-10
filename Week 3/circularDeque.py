class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = []
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        

    def insertFront(self, value: int) -> bool:
        if len(self.deque) == self.k:
            return False
        self.deque.insert(0, value)
        return True
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        

    def insertLast(self, value: int) -> bool:
        if len(self.deque) == self.k:
            return False
        self.deque.append(value)
        return True
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        

    def deleteFront(self) -> bool:
        if len(self.deque) == 0:
            return 0
        self.deque = self.deque[1:]
        return True
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        

    def getFront(self) -> int:
        if len(self.deque) > 0:
            return self.deque[0]   
        else:
            return -1
        """
        Get the front item from the deque.
        """
        

    def getRear(self) -> int:
        if len(self.deque) > 0:
            return self.deque[len(self.deque)-1]   
        else:
            return -1
        
        """
        Get the last item from the deque.
        """
        

    def isEmpty(self) -> bool:
        if len(self.deque) > 0:
            return False
        else:
            return True
        """
        Checks whether the circular deque is empty or not.
        """
        

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        else:
            return False
        """
        Checks whether the circular deque is full or not.
        """
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()