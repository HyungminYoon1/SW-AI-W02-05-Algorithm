# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

'''
풀이전략

맨 마지막 문자가 같으면 추가
같지 않으면 그 이전 비교
'''
'''
import sys
sys.setrecursionlimit(10**6)

first_str = input()
second_str = input()

idx1 = len(first_str) - 1
idx2 = len(second_str) - 1

dp = {} # ' (첫번째 문자열의 인덱스, 두번째 문자열의 인덱스) : LCS 길이 ' 형태로 딕셔너리에 저장

def compare(idx1, idx2):

    if idx1 < 0 or idx2 < 0:
        return 0

    if (idx1, idx2) in dp:
        return dp[(idx1, idx2)]
    
    result = 0

    if first_str[idx1] == second_str[idx2]:
        result = compare(idx1-1, idx2-1) + 1
        dp[(idx1, idx2)] = result
    else:
        if compare(idx1-1, idx2) > compare(idx1, idx2-1):
            bigger = compare(idx1-1, idx2)
            dp[(idx1-1, idx2)] = bigger
        else:
            bigger = compare(idx1, idx2-1)
            dp[(idx1, idx2-1)] = bigger

        result += bigger
        dp[(idx1, idx2)] = result

    return result

val = compare(idx1, idx2)
print(val)
'''
# 위 코드는 시간 초과로 백준 통과 실패


## gpt가 제시한 앞에서부터 점화식 풀이 -> 시간 초과로 백준 통과 실패
'''
import sys
sys.setrecursionlimit(10**6)

first_str = input()
second_str = input()

dp = {}

def compare(i, j):
    if i == len(first_str) or j == len(second_str):
        return 0

    if (i, j) in dp:
        return dp[(i, j)]

    if first_str[i] == second_str[j]:
        dp[(i, j)] = compare(i + 1, j + 1) + 1
    else:
        dp[(i, j)] = max(compare(i + 1, j), compare(i, j + 1))

    return dp[(i, j)]

result = compare(0, 0)
print(result)
'''

## gpt가 제시한 정석 풀이: 문자열 앞부분부터 점점 넓혀 가면서 채우는 방식


first_str = input()
second_str = input()

n = len(first_str)
m = len(second_str)
 
dp = [[0]*(m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if first_str[i - 1] == second_str[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])