class Stacks:
    def __init__(self, A):
        self.A = A[::-1]
    def fetch(self):                                                                                                                                                      
            return self.A.pop()
    def peek(self):
        if self.isEmpty():
            return 0
        else:
            return self.A[len(self.A) - 1]
    def isEmpty(self):
        if len(self.A) == 0:
            return True

l = Stacks([4, 2, 4, 6, 1])
k = Stacks([2])
j = Stacks([1,2])
count = 0
sum = 0
x = 10
a = 0
b = 0


if k.isEmpty() and (not (l.isEmpty())):
    a = l.fetch()
    count += 1
    #Do the fetching from l
elif l.isEmpty():
    #do the fetching from k
    a = k.fetch()
    count += 1
elif k.isEmpty() and l.isEmpty():
    print ('condition 1: gameover! Score is', count)

if l.peek() > k.peek() and (sum + k.peek() < x): # if k.peek() is the lowest available for take and adding it doesnt result in disqualification 
    a = k.fetch()
    count += 1
elif l.peek() <= k.peek() and (sum + l.peek() < x):
    a = l.fetch()
    count += 1
else:
    print ('condition 2: game over! your score is', count)
sum += a # Have to add everytime you fetch.

if k.isEmpty() and (not (l.isEmpty())):
    b = l.fetch()
    count += 1
    #Do the fetching from l
elif l.isEmpty():
    #do the fetching from k
    b = k.fetch()
    count += 1

if l.peek() > k.peek() and (sum + k.peek() < x): # if k.peek() is the lowest available for take and adding it doesnt result in disqualification 
    b = k.fetch()
    count += 1
elif l.peek() <= k.peek() and (sum + l.peek() < x):
    b = l.fetch()
    count += 1
else:
    print ('game over! your score is', count)

sum += b

print (a, b, sum)

