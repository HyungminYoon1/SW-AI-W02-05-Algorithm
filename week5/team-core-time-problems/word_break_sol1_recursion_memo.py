# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        memo = {}
        
        def dfs(sub_s):
            # 성공조건
            if sub_s == "":
                return True
            if sub_s in memo:
                return memo[sub_s]
            
            # 백트래킹
            for word in wordDict:
                if sub_s.startswith(word):
                    if dfs(sub_s[len(word):]): # 남은 문자열에서 재귀 호출
                        memo[sub_s] = True
                        return True
                    
            memo[sub_s] = False
            return False
        
        return dfs(s)