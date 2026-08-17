class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # stores temp index which - not found warmer temp
        output = [0]*len(temperatures)

        for i,t in enumerate(temperatures):

            while stack and temperatures[stack[-1]]< t:
                idx = stack.pop()
                output[idx] = i -idx
            stack.append(i)


        return output    




        