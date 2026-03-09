# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

def parse_numbers(line):
    return list(map(int, line.split()))

def get_student_ratio_over_average(score_infos):
    if len(score_infos) <= 1:
        return 0
    
    student_count = score_infos[0]
    student_scores = score_infos[1:]

    avg = sum(score_infos[1:]) / student_count

    avg_over_count = 0    
    for score in student_scores:
        if score > avg:
            avg_over_count += 1

    return avg_over_count / student_count * 100

test_case_count = int(input())
parsed_lines = []

for i in range(test_case_count):
    raw_line = input()
    parsed_lines.append(parse_numbers(raw_line))

for element in parsed_lines:
    line_result = get_student_ratio_over_average(element)
    print(f"{line_result:.3f}%")


## gpt 코칭 후 수정한 코드
'''
def get_student_ratio_over_average(scores):
    n = scores[0]
    student_scores = scores[1:]
    avg = sum(student_scores) / n
    over_count = sum(1 for score in student_scores if score > avg)
    return over_count / n * 100


t = int(input())

for _ in range(t):
    scores = list(map(int, input().split()))
    result = get_student_ratio_over_average(scores)
    print(f"{result:.3f}%")
'''

# 이 문제는 입력 1줄을 받자마자 바로 처리하면 되고, 굳이 전체를 저장할 이유가 없음