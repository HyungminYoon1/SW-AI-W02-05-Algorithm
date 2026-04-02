# https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:  # pyright: ignore[reportUndefinedVariable]
        
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0: # 행의 왼쪽 끝 선택
                    dp[i][j] = dp[i-1][j] + triangle[i][j] 
                elif j == len(triangle[i]) - 1: # 행의 오른쪽 끝 선택
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else: # 행의 중간(양 끝이 아닌 원소) 선택
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1]) # 마지막 줄에서 최소값 선택
        
        
        
        
        
        
        