class Solution:
    """ 
    O(C + Q) = O(V + E) time and space
    visited -> course added to order
    visiting -> course not added to order by added to cycle
    unvisited -> course not added to cycle or order
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.order = []

        preqMap = defaultdict(list)
        for c, q in prerequisites:
            preqMap[c].append(q)

        visit, cycle = set(), set()

        for n in range(numCourses):
            if not self.dfs(n, preqMap, visit, cycle):
                return []

        return self.order

    def dfs(self, course, preqMap, visit, cycle):
        if course in cycle:
            return False

        if course in visit:
            return True            

        cycle.add(course)

        for preq in preqMap[course]:
            if not self.dfs(preq, preqMap, visit, cycle):
                return False

        cycle.remove(course)
        visit.add(course)
        self.order.append(course)
        return True

        

        


        