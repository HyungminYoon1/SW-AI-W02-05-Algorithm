# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1) # 문자열의 처음부터 i번째 글자까지의 부분문자열이 wordDict의 단어들로 분해 가능한지 여부
        dp[0] = True # 빈 문자열은 항상 분해 가능
        
        for i in range(1, n + 1):
            for j in range(i):
                # dp[j]가 True이고, s[j:i]가 word_set에 있으면, dp[i]를 True로 설정
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
        