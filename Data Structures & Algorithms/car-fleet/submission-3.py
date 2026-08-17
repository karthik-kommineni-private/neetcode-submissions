class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #stores time to reach dest for all cars, update stack -if collide
        
        # Sort cars by position in descending order (closest to target first)
        combined = sorted(zip(position, speed), reverse=True)

        for p, s in combined:
            rem_dist = target - p
            curr_time = rem_dist / s

            # If stack is empty or curr_time is greater than the fleet ahead,
            # this car starts a new fleet.
            if not stack or curr_time > stack[-1]:
                stack.append(curr_time)

        return len(stack)