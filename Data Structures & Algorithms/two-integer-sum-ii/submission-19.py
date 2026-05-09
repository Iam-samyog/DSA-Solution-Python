class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Optimal Solution
        #using two pointer

        hash={}

        for i in range(len(numbers)):
            remainder=target-numbers[i]
            if remainder in hash:
                return [hash[remainder]+1,i+1]
            hash[numbers[i]]=i
            
           
            
                