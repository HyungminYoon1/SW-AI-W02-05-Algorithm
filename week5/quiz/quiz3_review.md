# 문제
3.어떤 사람이 한 번에 1칸 또는 2칸을 올라갈 수 있는 계단이 있다. 계단의 총 개수 N이 주어졌을 때, 이 사람이 계단을 올라가는 서로 다른 방법의 수를 구하는 프로그램을 반복문과 DP를 이용하여 파이썬으로 작성하시오. 

# 함수의 리턴 : 서로 다른 방법의 수

    # n은 1 이상의 값으로 가정

    def climb_stairs(n: int) -> int:

        # DP 테이블 초기화

        dp = [0] * (n + 1)

        

        # 함수의 나머지를 작성

---

# 답변
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]

---

# 정답
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

return dp[n]