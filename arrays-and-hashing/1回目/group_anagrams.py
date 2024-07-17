from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs_dict = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            sorted_strs_dict[s].append(strs[i])
        
        res = list()
        for _, vs in sorted_strs_dict.items():
            tmp = []
            for v in vs:
                tmp.append(v)
            res.append(tmp)
        
        return res

inputs = list(input().split())
s = Solution()
print(s.groupAnagrams(inputs))