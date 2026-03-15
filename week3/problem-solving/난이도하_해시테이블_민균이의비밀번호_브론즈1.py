# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

'''
단어가 한 줄에 하나씩
모든 단어의 길이는 홀수
비밀번호 및 비밀번호를 뒤집어서 쓴 문자열도 목록에 포함
모두 비밀번호로 사용 가능

요구사항: 비밀번호의 길이와 가운데 글자를 출력
'''

line_count = int(input())
line_texts = set()
for i in range(line_count):
    line_texts.add(input())

count = len(line_texts)
for line_text in line_texts:
    if line_text[::-1] in line_texts:
        result_length = len(line_text)
        middle_char = line_text[len(line_text)//2]
        print(result_length, middle_char)
        break
