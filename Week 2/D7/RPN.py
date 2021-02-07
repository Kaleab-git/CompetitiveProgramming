class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.numbers = []
        for i in tokens:
            if i not in "+/*-":
                self.numbers.append(i)
            else:
                n1 = int(self.numbers.pop())
                n2 = int(self.numbers.pop())
                result = self.operate(n2, n1, i)
                self.numbers.append(result)
        return self.numbers.pop()
    
    def operate(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1*num2
        else:
            if abs(num1) < abs(num2):
                return 0
            else:
                return int(num1/num2)
            
            

            
        