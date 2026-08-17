from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)

        def cycle(crs: int, seen: set) -> bool:
            if crs in seen:
                return True  # cycle detected

            # If already processed and has no prereqs, no cycle from here
            if not preMap[crs]:
                return False

            seen.add(crs)
            for preq in preMap[crs]:
                if cycle(preq, seen):   # <-- key fix
                    return True

            seen.remove(crs)
            preMap[crs] = []  # memoize as "safe"
            return False

        seen = set()
        for c in range(numCourses):
            if cycle(c, seen):
                return False
        return True

'''
Course Schedule — Summary

1. This is cycle detection in a directed graph.
2. Build an adjacency list where course → prerequisites.
3. Use DFS with a recursion stack to detect cycles.
4. If a node is seen again in the current DFS path, a cycle exists.
5. Memoize nodes proven safe to avoid recomputation.
6. Earlier mistake: returned False when prerequisites were empty (should be True).
7. Earlier mistake: used only one visited state without memoization.
8. Earlier mistake: defaultdict mutated during iteration.
9. Time Complexity: O(numCourses + prerequisites).
10. Space Complexity: O(numCourses + prerequisites).
'''
