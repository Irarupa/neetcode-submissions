class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         freq_ict = {}
         n = len(nums)
         for num in nums:
            freq_ict[num] = freq_ict.get(num,0)+1

         res = next((key for key,value in freq_ict.items() if value >n/2),None)
         return res
         