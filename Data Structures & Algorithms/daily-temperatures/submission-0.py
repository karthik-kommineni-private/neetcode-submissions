class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # indices
        output = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                ind = stack.pop()
                output[ind] = i - ind
            stack.append(i)
        return   output      





        