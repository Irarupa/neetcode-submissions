class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         maxcount = 0
         n = len(nums)

         for i  in range(0,n):
            num = nums[i]
            count = 1

            while num+1 in nums:
                count+=1
                num = num+1
            maxcount = max(maxcount,count)

         return maxcount

