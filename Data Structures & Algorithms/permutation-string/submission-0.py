class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         s_1 = {}

         for i in range(len(s1)):
            s_1[s1[i]] = s_1.get(s1[i],0)+1
         

         for j in range(len(s2)-len(s1)+1):
                s_2 = {}

                window = s2[j:j+len(s1)]
                for ch in window:
                    s_2[ch] = s_2.get(ch,0)+1
                    if s_2 == s_1:
                      return True

         return False



