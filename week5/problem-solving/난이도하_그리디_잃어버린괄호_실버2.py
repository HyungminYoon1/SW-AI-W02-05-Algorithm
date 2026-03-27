# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

'''
풀이전략

'(' 가 들어가는 위치는 + 와 숫자 사이 또는 - 와 숫자 사이가 될 수 있다.
그러나 총합의 최솟값을 만들기 위해서는 - 와 숫자 사이에 '(' 을 넣고 그 다음 수를 찾다가 
다음 - 가 나오기 직전에 ')' 를 넣어 총합에서 빼는 숫자들의 합을 극대화시키는 것이 좋다.
'''

# - 기준으로 입력값 문자열을 쪼갠 리스트
parts = list(input().split("-"))

# 초기값 구하기(최초의 - 가 등장하기 전까지의 총합)
nums = list(map(int, parts[0].split("+"))) # 최초 원소를 + 기준으로 쪼개고 정수로 매핑
result = sum(nums)

# -를 찾으면 그 다음 -가 나오기 전까지 숫자의 총합을 초기값에서 계속 빼야 한다.
for part in parts[1:]:
    result -= sum(map(int, part.split("+")))

print(result)