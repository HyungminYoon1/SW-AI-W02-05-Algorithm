# https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            raise ValueError("N should be a natural number.")
        if n <= 2:
            return n
        
        a, b = (1, 2)

        for i in range(3, n+1):
            a, b = b, a+b

        return b

