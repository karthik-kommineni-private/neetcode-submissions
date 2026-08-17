class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack = []
        for i in range(len(op)):    
            
            if op[i] == "+":
               stack.append(int(stack[-1]+ stack[-2]))

            elif op[i] == "D":
                stack.append(int(2 * stack[-1]))

            elif op[i] == "C":
                stack.pop()

            else:
                stack.append(int(op[i]))

        return sum(stack)        





        