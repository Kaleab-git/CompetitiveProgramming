class MyQueue(object):

    def __init__(self):
        self.s1 = [] #storing stack
        self.s2 = [] #operation stack
        
    def push(self, x):
        self.s1.append(x)
    
    def pop(self):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        self.s2.clear()
        return temp
            

    def peek(self):
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        self.s1.append(temp)
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        self.s2.clear()
        return temp
    
    def empty(self):
        if len(self.s1) == 0:
            return True
        else:
            return False

q = MyQueue()

q.push(1);q.push(2);q.push(3);q.push(4);q.push(5)
print (q.empty())
q.peek();q.peek();q.peek();q.peek();q.peek()
print (q.empty())
for i in range(5):
    print (q.pop())
print (q.empty())

