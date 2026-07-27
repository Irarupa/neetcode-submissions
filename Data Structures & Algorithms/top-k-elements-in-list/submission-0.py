class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        rs = []
        maxl = 0
        n= len(nums)
        for i in range(n):
            count[nums[i]] = count.get(nums[i],0)+1
        while(k>0):
            maxl = max(count, key=count.get)
            count.pop(maxl)
            rs.append(maxl)
            k-=1  
        return rs             


            


       