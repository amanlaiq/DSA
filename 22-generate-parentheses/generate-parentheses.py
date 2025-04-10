# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         stack = []

#         def backtrack(openn, closedn):
#             if openn == closedn == n:
#                 res.append("".join(stack))

#             if openn < n:
#                 stack.append("(")
#                 backtrack(openn + 1, closedn)
#                 stack.pop()
            
#             if closedn < n:
#                 stack.append(")")
#                 backtrack(openn, closedn + 1)
#                 stack.pop()
        
#         backtrack(0,0)
#         return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openn, closedn):
            if openn == closedn == n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append("(")
                backtrack( openn + 1, closedn)
                stack.pop()

            if closedn < openn:
                stack.append(")")
                backtrack(openn, closedn + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        