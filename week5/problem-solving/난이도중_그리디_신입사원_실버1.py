# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

test_case_count = int(input())
result = []

for _ in range(test_case_count):
    candidates_count = int(input())

    scores = []

    for _ in range(candidates_count):
        docs, interview = map(int, input().split())
        scores.append((docs, interview))
    
    sorted_scores = sorted(scores, key=lambda x: x[0]) # 서류 순위 오름차순으로 정렬
    # sorted_interview_score = sorted(scores, key=lambda x: x[1]) # 면접 순위로 정렬해서 서류를 심사하는 방식도 가능

    count = 1
    best_interview = sorted_scores[0][1] # 서류 최고순위자의 면접순위 초기화

    for i in range(1, len(sorted_scores)):
        if sorted_scores[i][1] < best_interview:
            count += 1
            # 면접 최고순위 갱신
            best_interview = sorted_scores[i][1]
    
    result.append(count)

for value in result: 
    print(value)