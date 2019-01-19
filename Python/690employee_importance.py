"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        emap = {}
        for employee in employees:
            emap[employee.id] = [employee.importance, employee.subordinates]

        importance = emap[id][0]
        subordinates = emap[id][1]

        while subordinates:
            new_subordinates = []
            for subordinate in subordinates:
                importance += emap[subordinate][0]
                new_subordinates += emap[subordinate][1]
            subordinates = new_subordinates

        return importance
