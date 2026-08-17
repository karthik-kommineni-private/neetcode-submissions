class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for c in asteroids:
            if c >= 0:
                stack.append(c)
            else:    
                while stack and c< 0 and stack[-1] > 0:
                    if stack[-1] ==  abs(c): 
                        stack.pop()
                        continue
                    elif stack[-1] < abs(c):
                        stack.pop()
                    else:
                        break  
        return stack