# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rob(self, nums) -> int:
        
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            # 현재 집을 털지 않으면: 바로 이전 집까지의 최댓값 유지
            # 현재 집을 털면: 이전 집까지의 최댓값 + 현재 집의 돈
            # 둘 중 큰 값을 선택
            
        return dp[n-1]