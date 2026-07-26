class Solution:
    def minWindow(self, s: str, t: str) -> str:
         hash = [0]*256
         l =0
         r =0
         sindex = -1
         minlen = float('inf')
         m = len(t)
         count = 0
         n = len(s)
         for i in range(m):
            hash[ord(t[i])] +=1
         while r<n:
            if hash[ord(s[r])]>0:
                count +=1
            hash[ord(s[r])]-=1
            while(count == m):
                if (r-l+1<minlen):
                     minlen = r-l+1
                     sindex = l
                hash[ord(s[l])]+=1
                if hash[ord(s[l])] >0: 
                  count = count-1
                l +=1
            r +=1
         if sindex ==-1:
            return ""
         return s[sindex:sindex+minlen]                 


