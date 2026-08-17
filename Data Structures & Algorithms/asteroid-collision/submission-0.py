class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            #if stack is empty
            if not stack:
                stack.append(x)
                continue
            elif x > 0:
                stack.append(x)
            else:
                if stack[-1] > abs(x):
                    continue
                elif  stack[-1] == abs(x):  
                    stack.pop() 
                else:
                    stack.pop()
                    stack.append(x)  

        return stack              

