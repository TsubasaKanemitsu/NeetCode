class Solution:
    def isValid(self, s: str) -> bool:
        stack = list(s[0])
        open_brackets = {
            ")": "(",
            "}" : "{",
            "]" : "["
        }
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if stack[-1] == open_brackets.get(s[i], ""):
                stack.pop(-1)
            else:
                stack.append(s[i])
        return len(stack) == 0
    
s = Solution()
print(s.isValid('(){}}{'))