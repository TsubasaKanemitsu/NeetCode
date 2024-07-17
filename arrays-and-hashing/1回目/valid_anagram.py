from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt_s, cnt_t = {}, {}

        for i in range(len(s)):
            cnt_s[s[i]] = 1 + cnt_s.get(s[i], 0)
            cnt_t[t[i]] = 1 + cnt_t.get(t[i], 0)

        for k in cnt_s:
            if cnt_s[k] != cnt_t.get(k, 0):
                return False
            
        return True

input_s = input()
input_t = input()

s = Solution()
print(s.isAnagram(input_s, input_t))