class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        result = len(temperatures)*[0]
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                result[stack[-1][0]] = i-stack[-1][0]  
                stack.pop()
            stack.append((i,t))       
        return result