# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493


# 자신보다 큰 왼쪽에 있는 수 중, 가장 가까운 수 찾기: 해당 숫자 인덱스+1 로 반환. 없으면 0 반환.

tower_count = int(input())

towers = list(map(int, input().split()))
stack = []  # (index, height)  아직 오른쪽 탑들의 신호를 받을 가능성이 남아 있는 왼쪽 탑들을 쌓아둔 것
result = []

for i, height in enumerate(towers):
    while stack and stack[-1][1] < height:
        stack.pop() # 현재 탑보다 낮은 탑은 현재 탑에 가려져 이후에도 수신 후보가 될 수 없으므로 제거
    
    if stack:
        result.append(stack[-1][0] + 1) # 스택에 탑이 있다면 가장 왼쪽의 탑(현재 탑보다 높음)의 인덱스 +1 을 입력
    else:
        result.append(0) # 없으면 0 입력

    stack.append((i, height)) # 검토가 끝난 현재 탑도 이후 탑들의 후보가 되므로 스택에 추가

print(' '.join(map(str, result)))