from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()  # nodes in current DFS path
        visited = set()   # nodes already proven safe

        def dfs(course: int) -> bool:
            # cycle detected
            if course in visiting:
                return False

            # already checked and safe
            if course in visited:
                return True

            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)

            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
