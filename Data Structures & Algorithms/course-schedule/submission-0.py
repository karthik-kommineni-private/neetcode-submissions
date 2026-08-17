class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites is None or len(prerequisites) == 0 :
            return False

        visit = set()

        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course):

            if course in visit:
                return False  

            if preMap[course] == []:
                return True      
            visit.add(course)    
            
            b = True
            for pre in preMap[course]:
                b = b and dfs(pre)    

            visit.remove(course)
            return b


        b = True
        for course in preMap:
            b = b and dfs(course) 
        return b       







        