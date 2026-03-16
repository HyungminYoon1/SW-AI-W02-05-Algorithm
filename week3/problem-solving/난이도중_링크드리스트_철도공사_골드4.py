# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

'''
고유 번호 i 다음 고유 번호를 출력, 그 사이에 고유 번호 j 추가
고유 번호 i 이전 고유 번호를 출력, 그 사이에 고유 번호 j 추가
고유 번호 i 다음 번호를 제거, 제거된 고유 번호를 출력
고유 번호 i 이전 번호를 제거, 제거된 고유 번호를 출력

고유 번호는 최대 1회만 사용, 제거했던 고유 번호는 다시 추가 가능
고유 번호 제거는 남은 고유 번호가 2개 이상이어야 함.

'''

import sys
input = sys.stdin.readline

next_station = {}
prev_station = {}
results = []

def put_station_info(num_list):
    n = len(num_list)
    for i in range(0, n-1):
        next_station[num_list[i]] = num_list[i+1]
        prev_station[num_list[i+1]] = num_list[i]
    next_station[num_list[n-1]] = num_list[0]
    prev_station[num_list[0]] = num_list[n-1]

def station_construct(action_code):

    action_code = list(action_code.split())
    
    i = int(action_code[1])
    
    if action_code[0] == 'BN':
        j = int(action_code[2])
        k = next_station[i]
        results.append(str(k))

        next_station[i] = j
        next_station[j] = k
        prev_station[j] = i
        prev_station[k] = j
        
    elif action_code[0] == 'BP':
        h = int(action_code[2])
        g = prev_station[i]
        results.append(str(g))

        next_station[h] = i
        next_station[g] = h
        prev_station[h] = g
        prev_station[i] = h

    elif action_code[0] == 'CN':
        j = next_station[i] # 삭제 대상
        k = next_station[j]

        next_station[i] = k
        prev_station[k] = i
        
        results.append(str(j))
        del next_station[j]
        del prev_station[j]

    elif action_code[0] == 'CP':
        h = prev_station[i] # 삭제 대상
        g = prev_station[h]

        next_station[g] = i
        prev_station[i] = g

        results.append(str(h))
        del next_station[h]
        del prev_station[h]
    
    else:
        return

station_count_n, action_count_m = map(int, input().split())
stations = list(map(int, input().split()))

put_station_info(stations)

for _ in range(action_count_m):
    station_construct(input())

print('\n'.join(results))

'''
시간 초과로 백준 통과 실패
'''

## gpt가 개선한 코드(Python3는 시간초과로 실패, PyPy3는 통과)

import sys

read = sys.stdin.buffer.readline
write = sys.stdout.write

MAX_ID = 2000000
prev_station = [0] * (MAX_ID + 1)
next_station = [0] * (MAX_ID + 1)

n, m = map(int, read().split())
stations = list(map(int, read().split()))

prev = prev_station
nxt = next_station

first = stations[0]
last = first

for cur in stations[1:]:
    nxt[last] = cur
    prev[cur] = last
    last = cur

nxt[last] = first
prev[first] = last

out = []
append = out.append

for _ in range(m):
    cmd = read().split()
    op = cmd[0]
    i = int(cmd[1])

    if op == b'BN':
        j = int(cmd[2])
        k = nxt[i]
        append(str(k))

        nxt[i] = j
        prev[j] = i
        nxt[j] = k
        prev[k] = j

    elif op == b'BP':
        j = int(cmd[2])
        g = prev[i]
        append(str(g))

        nxt[g] = j
        prev[j] = g
        nxt[j] = i
        prev[i] = j

    elif op == b'CN':
        j = nxt[i]
        k = nxt[j]
        append(str(j))

        nxt[i] = k
        prev[k] = i

    else:  # CP
        j = prev[i]
        g = prev[j]
        append(str(j))

        nxt[g] = i
        prev[i] = g

write('\n'.join(out))