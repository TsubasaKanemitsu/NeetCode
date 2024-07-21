from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []
        # N = 2 * n
        # for bit in range(1 << N):
        #     op = 0
        #     p = ""
        #     for i in range(N):
        #         if bit & (1 << i):
        #             op -= 1
        #             p += ")"
        #         else:
        #             op += 1
        #             p += "("
        #         if op < 0:
        #             break
        #     if op == 0:
        #         res.append(p)
        # return res
        
        res = []
        stack = []

        def backtrack(open: int, close: int, N: int):
            if open < close:
                return
            
            if len(stack) == N:
                if open == close:
                    res.append(''.join(stack))
                return

            stack.append("(")
            backtrack(open + 1, close, N)
            stack.pop()

            stack.append(")")
            backtrack(open, close + 1, N)
            stack.pop()

        backtrack(0, 0, 2*n)
    
        return res

s = Solution()
print(s.generateParenthesis(3))
