class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         count = {}

         for word in strs:
            arr = [0]*26
            for ch in word:
                arr[ord(ch)-ord('a')]+=1
            key = tuple(arr)

            if key not in count:
              count[key] = []
            count[key].append(word)
         return list(count.values())
        

