from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)

        for s in strs:
            key=sorted(s)
            groups[tuple(key)].append(s)
        
        return list(groups.values())

        