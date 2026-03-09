# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

case_count = int(input())
result_list = []

for i in range(case_count):
    line_texts = input().split(" ")
    repeat_count = int(line_texts[0])
    pure_text = line_texts[1]
    text_count = len(pure_text)
    result = ""
    for char in pure_text:
        result = result + char*repeat_count
    result_list.append(result)

for element in result_list:
    print(element)


## gpt 코칭 후 수정한 코드
'''
case_count = int(input())

for _ in range(case_count):
    r, s = input().split()
    r = int(r)
    print("".join(c*r for c in s))
'''