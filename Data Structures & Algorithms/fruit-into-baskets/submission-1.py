class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        max_num=0
        for i in range(len(fruits)):
            seen=set()
            for j in range(i,len(fruits)):
                seen.add(fruits[j])

                if len(seen)<=2:
                    max_num=max(max_num,j-i+1)
                else:
                    break
        
        return max_num