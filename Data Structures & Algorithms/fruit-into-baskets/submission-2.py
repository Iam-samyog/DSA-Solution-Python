class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        max_fruit=0
        
        for i in range(len(fruits)):
            seen=set()
            for j in range(i,len(fruits)):
                seen.add(fruits[j])
                if len(seen)>2:
                    break
                max_fruit=max(max_fruit,j-i+1)
        
        return max_fruit