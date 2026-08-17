class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add openParenthesisCount when opc < n
        # add cpc when cpc < opc
        # base case if opc == cpc == n

        stack = []

        res = []

        def addParenthesisIfValid(opc, cpc):
            #base case
            if opc == cpc == n:
                validString = "".join(stack)  # why not join()
                res.append(validString)
                return

            #set of conditions
            if opc < n:
                stack.append("(")
                addParenthesisIfValid(opc+1, cpc)
                stack.pop()

            if cpc < opc:
                stack.append(")")
                addParenthesisIfValid(opc, cpc+1)
                stack.pop()

        addParenthesisIfValid(0,0)
        return res   
        