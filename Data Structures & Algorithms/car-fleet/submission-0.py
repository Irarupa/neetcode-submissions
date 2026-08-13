class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s1 = []
        a = sorted(zip(position, speed), reverse=True)

        for i in range(len(a)):
                position,speed = a[i]
                mul = (target-position)/speed
                if not s1 or  mul > s1[-1] :
                    s1.append(mul)
        return len(s1)
