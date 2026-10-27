class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        count=defaultdict(list)

        for x in strs:
            key=tuple(sorted(x))
            count[key].append(x)
        
        return list(count.values())

        
