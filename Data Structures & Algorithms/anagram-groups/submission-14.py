class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res=defaultdict(list)

        for x in strs:
            key=tuple(sorted(x))
            res[key].append(x)
        
        return list(res.values())
