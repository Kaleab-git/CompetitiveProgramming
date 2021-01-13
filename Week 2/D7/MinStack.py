class MinStack(object):

    def __init__(self):
        self.stack_list = []

    def push(self, x):
        self.stack_list.append(x)
        
    def pop(self):
        return self.stack_list.pop()

    def top(self):
        return self.stack_list[len(self.stack_list)-1]
        

    def getMin(self):
        return min(self.stack_list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()