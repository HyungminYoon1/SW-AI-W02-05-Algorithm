# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700



'''
풀이 전략
처음에 서로 다른 가전제품 종류 n개가 플러그에 꽂힐 때까지 대기열을 넘긴다.
남아있는 대기열을 한 칸씩 탐색하면서 플러그에 있지 않은 새로운 아이템이 나올 때까지 탐색한다.
새로운 아이템이 나올 경우, 현재 꽂혀 있는 것 중 앞으로 가장 나중에 다시 쓰이거나, 아예 다시 안 쓰이는 것이 존재할 경우 그것을 뽑고 새로운 아이템으로 교체한다.
위의 과정을 k개의 대기열을 모두 사용할 때까지 반복한다.

'''

n, k = map(int, input().split()) # n: 멀티탭 구멍 갯수, k: 전기 용품의 총 사용횟수
item_order_list = list(map(int, input().split())) # 순서 대기열
power_strip = set() # 현재 멀티탭에 꽂혀있는 플러그 상태
plug_out_count = 0 # 플러그를 뽑은 횟수

for i in range(k):
    current_item = item_order_list[i]

    if current_item in power_strip: # 이미 멀티탭에 있는 아이템이면 통과
        continue

    if len(power_strip) < n:
        power_strip.add(current_item) # 신규 아이템이고 멀티탭에 자리가 비어있으면 추가
        continue

    target = None
    farthest_idx = -1

    for item in power_strip:

        next_idx = -1 # 현재 멀티탭의 아이템이 다음에 언제 사용되는지 순서 리스트에서 인덱스 확인
        for j in range(i + 1, k):
            if item_order_list[j] == item:
                next_idx = j
                break
        
        # 현재 아이템이 향후 사용하지 않을 경우 곧바로 제거 대상이 됨
        if next_idx == -1:
            target = item
            break
            
        # 2순위 타겟: 향후 가장 늦게 사용하는 플러그를 찾음
        if next_idx > farthest_idx:
            farthest_idx = next_idx
            target = item

    power_strip.remove(target)
    power_strip.add(current_item)
    plug_out_count += 1

print(plug_out_count)

'''
현재 코드는 O(k * n) 수준으로 뒤쪽 구간을 선형 탐색하고 있어서 시간복잡도는 대략 O(k * n * k)에 가깝습니다.

더 나은 구현이 존재하며 그 방법은 다음과 같습니다.
- 각 전자제품이 앞으로 등장하는 인덱스들을 미리 저장
- 현재 시점이 지나면 그 인덱스를 pop
- 멀티탭에 꽂힌 것들 중 다음 등장 인덱스가 가장 큰 것, 또는 더 이상 안 나오는 것을 제거

이렇게 하면 전체 시간복잡도가 O(k * n) 수준으로 내려갑니다.
최적화 포인트는 다음 등장 위치를 매번 찾지 말고 미리 관리하는 것입니다.
'''

## gpt가 제시한 최적 풀이

from collections import defaultdict, deque

n, k = map(int, input().split())
order = list(map(int, input().split()))

future = defaultdict(deque)
for idx, item in enumerate(order):
    future[item].append(idx)

power_strip = set()
plug_out_count = 0

for idx, current_item in enumerate(order):
    future[current_item].popleft()

    if current_item in power_strip:
        continue

    if len(power_strip) < n:
        power_strip.add(current_item)
        continue

    target = None
    farthest_idx = -1

    for item in power_strip:
        if not future[item]:
            target = item
            break

        next_idx = future[item][0]
        if next_idx > farthest_idx:
            farthest_idx = next_idx
            target = item

    power_strip.remove(target)
    power_strip.add(current_item)
    plug_out_count += 1

print(plug_out_count)
