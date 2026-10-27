class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        x = 0
        while len(stones)>1:
           stones.sort(reverse = True)
           if stones[0]>stones[1]:
              x = stones[0]-stones[1]
              del stones[0]
              del stones[0]
              stones.append(x)

           elif stones[0]==stones[1]:
              del stones[0]
              del stones[0]
        return stones[0] if stones else  0


        