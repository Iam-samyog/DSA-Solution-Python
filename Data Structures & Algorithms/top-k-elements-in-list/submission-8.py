class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap={}
        freq=[[] for i in range(len(nums)+1)]

        for c in nums:
            hashMap[c]=1+hashMap.get(c,0)

        for n,c in hashMap.items():
            freq[c].append(n)


        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        
        
        