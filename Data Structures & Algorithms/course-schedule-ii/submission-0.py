class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = defaultdict(list)
        for c,p in prerequisites:
            preMap[c].append(p)


        order = []    
        visited = set() #processed - no need for dfs again/can be done by emptying map -> list
        visiting = set() #stacktrace of visting path

        def cycle_dfs(course):
            if course in visiting:
                return True #cycle detected

            if course in visited:
                return False #already processed - we know its good/no cycle-reduce work

            visiting.add(course)
            preq = preMap[course]
            for p in preq:
                if cycle_dfs(p):   #process neighbours/prequistes
                   return True

            visiting.remove(course) #clearing for other paths
            order.append(course)
            visited.add(course)
            return False         


        for c in range(numCourses):
            if cycle_dfs(c):
                return []
        return order        


'''
Course Schedule II — Summary

1. This problem is topological sorting of a directed graph.
2. Each course is a node; each prerequisite is a directed edge.
3. Use DFS with a recursion stack to detect cycles.
4. `visiting` tracks the current DFS path (cycle detection).
5. `visited` marks courses already fully processed and safe.
6. If a course is seen again in `visiting`, a cycle exists → return [].
7. Add a course to the order only after all prerequisites are processed (postorder).
8. Earlier mistake: returned result inside the loop, processing only one course.
9. Time Complexity: O(numCourses + prerequisites).
10. Space Complexity: O(numCourses + prerequisites).
'''
  