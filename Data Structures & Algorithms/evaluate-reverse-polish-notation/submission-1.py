class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            
            if x == "+":
                stack.append(stack[-1]+stack[-2])

            elif x == "-":
                stack.append(stack[-2]-stack[-1])

            elif x == "*":
                stack.append(stack[-1]*stack[-2])

            elif x == "/":
                stack.append(stack[-2]/stack[-1])
            
            else:
                stack.append(int(x))
            
            
        return stack[-1]
 








        #edge
        