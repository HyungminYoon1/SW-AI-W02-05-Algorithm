# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 총 테스트케이스의 수
test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split()) # 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 

    min_flight_count = n-1 # 모든 정점을 방문 가능하게 만드는 최소 간선 수는 항상 n - 1

    for _ in range(m):
        t = input()
    
    print(min_flight_count)
        

