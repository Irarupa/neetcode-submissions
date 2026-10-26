class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         count = {}
         for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right],0)+1

         result = len(count)>0 and max(count.values())>1
         return result
