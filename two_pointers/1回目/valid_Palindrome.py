class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 愚直解
        # lower_s = s.lower()
        # ss = ""
        # for ls in lower_s:
        #     if self.isAlphaNumeric(ls):
        #         ss += ls
        # return ss == ss[::-1]

        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                    l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                    r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

    def isAlphaNumeric(self, s:str) -> bool:
        if ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9'):
            return True
        return False

sl = Solution()
s=",,,,"
print(sl.isPalindrome(s))