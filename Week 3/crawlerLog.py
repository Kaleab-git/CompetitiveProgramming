class Solution:
    def minOperations(self, logs: List[str]) -> int:
        self.depth = 0
        for i in logs:
            if i == "../":
                if self.depth > 0:
                    self.depth -= 1
            elif i == "./":
                continue
            else:
                self.depth += 1
        return self.depth        
        