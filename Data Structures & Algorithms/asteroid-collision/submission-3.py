class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for c in asteroids:

            while stack and stack[-1] > 0 and c < 0:

                if stack[-1] < -c:
                    stack.pop()
                    continue

                elif stack[-1] == -c:
                    stack.pop()
                    c = 0
                    break

                else:
                    c = 0
                    break

            if c != 0:
                stack.append(c)

        return stack