# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

'''
풀이전략: 가장 빨리 끝나는 미팅을 먼저 고려하여 배정 -> 그리디
'''

n = int(input())

meeting_list = []

for i in range(n):
    start_time, end_time = map(int, input().split())
    meeting_list.append((start_time, end_time)) # 튜플로 저장

meeting_list = sorted(meeting_list, key=lambda x: (x[1], x[0])) # 종료시간 기준으로 1차 오름차순 소팅, 시작시간 기준으로 2차 오름차순 소팅

# 방어 코드
if len(meeting_list) <= 1:
    print(len(meeting_list))
    exit()

selected_meeings = [meeting_list[0]]

for i in range(1, len(meeting_list)):
    former_meeting_end_time = selected_meeings[-1][1]
    current_start_time = meeting_list[i][0]
    if current_start_time >= former_meeting_end_time:
        selected_meeings.append(meeting_list[i])

print(len(selected_meeings))
