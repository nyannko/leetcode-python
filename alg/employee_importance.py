"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for e in employees:
            d[e.id] = e
        if id not in d:
            return
        return self.dfs(d, d[id])

    def dfs(self, d, e):
        res = e.importance
        for i in e.subordinates:
            res += self.dfs(d, d[i])
        return res
