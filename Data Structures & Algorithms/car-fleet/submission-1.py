class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #stores time to reach dest for all cars, update stack -if collide
        count = 0

        for p,s in zip(sorted(position),sorted(speed)):
            rem_dist = target-p
            curr_time = rem_dist/s

            while stack and curr_time >= stack[-1]:
                stack.pop()      
            stack.append(curr_time)       
            count+=1    

        return count-2

'''
#0 1 4 7
#1 2 2 1

#10 4.5 3 3 4

#stack(3 )
# count 3
'''