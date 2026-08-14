class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
         s1 = []
         for i in range(len(nums)):
            s1.append(nums[i])
         

         num = nums+s1
         return num
        