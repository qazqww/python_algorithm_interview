from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = defaultdict(list)
        for st in strs:
            dic[''.join(sorted(st))].append(st)
        return list(dic.values())

# ''.join과 sorted의 활용 익히기

Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
Solution().groupAnagrams([""])
Solution().groupAnagrams(["a"])