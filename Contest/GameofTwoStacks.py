class Stacks:
    def __init__(self, A):
        self.A = A
        self.index = 0
    def fetch(self):
        return self.A.pop(self.index)

    def move(self):
        self.index += 1
        return self.index

    def isEmpty(self):
        if len(self.A == 0):
            return True

l = Stacks([1,2,3,3,5])


print (l.fetch())
print (l.fetch())
print (l.fetch())
print (l.fetch())
print (l.A)