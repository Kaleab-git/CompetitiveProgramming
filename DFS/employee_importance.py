"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_importance = 0
        subordinates_dictionary = {}
        importance_dictionary = {}
        
        for employee in employees:
            if employee.id == id:
                emp = employee
                total_importance += employee.importance
            subordinates_dictionary[employee.id]=employee.subordinates
        for employee in employees:
            importance_dictionary[employee.id]=employee.importance
        queue = [id]
        
        while queue:
            id = queue.pop()
            for subordinates in subordinates_dictionary[id]:
                total_importance += importance_dictionary[subordinates]
                queue.append(subordinates)
        return total_importance
        
        
        
        
        
        
        
        
        
        
        