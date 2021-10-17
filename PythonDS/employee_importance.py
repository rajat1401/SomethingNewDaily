#priblem link: https://leetcode.com/problems/employee-importance/
#problem statement: big

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class EmployeeImportance:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dictt= {}
        for employee in employees:
            dictt[employee.id]= employee
        q= [id]
        summ= 0
        while(q):
            a= q.pop(0)
            summ+= dictt[a].importance
            for subs in dictt[a].subordinates:
                q.append(subs)
        return summ