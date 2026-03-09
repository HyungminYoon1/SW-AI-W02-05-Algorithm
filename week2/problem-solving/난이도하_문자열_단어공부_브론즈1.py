# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

raw_text = input()
char_count = {}

for char in raw_text:
    char = char.upper()
    if char_count.get(char) == None:
        char_count[char] = 1
    else:
        char_count[char] += 1
    
def get_max_val_key(dictionary):
    if len(dictionary) == 0:
        return ""
    
    if len(dictionary) == 1:
        return next(iter(dictionary))
    
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    max_key, max_value = sorted_items[0]
    second_key, second_value = sorted_items[1]

    if max_value == second_value:
        return "?"
    
    return max_key

print(get_max_val_key(char_count))

# 현재 코드의 비효율/문제점
'''
1. 정렬을 전체에 수행함
sorted_items = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

이 문제에서 필요한 것은 사실상 가장 큰 빈도, 그 최대 빈도를 가진 문자가 여러 개인지 여부 뿐임.
- 정렬 사용: O(k log k)
- 최대값만 찾기: O(k)

2. 2. 함수가 매개변수를 안 쓰고 바깥 변수 char_count를 참조함
def get_max_val_key(dictionary):
    ...
    sorted_items = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

함수 인자로 dictionary를 받았는데 실제로는 char_count를 사용합니다.
즉, 함수가 외부 상태에 의존하고 있습니다.  

*=> 의도한 동작이 아니고, 놓치고 미처 수정하지 못한 변수명이라 다시 수정

3. == None 보다 is None 이 더 적절함

'''

## gpt 코칭 후 수정한 코드
raw_text = input().upper()
char_count = {}

for char in raw_text:
    char_count[char] = char_count.get(char, 0) + 1

max_count = max(char_count.values())
max_chars = [char for char, count in char_count.items() if count == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0])


## gpt가 제안한 최적의 코드
word = input().upper()
char_count = {}

for char in word:
    char_count[char] = char_count.get(char, 0) + 1

max_count = max(char_count.values())

answer = []
for char, count in char_count.items():
    if count == max_count:
        answer.append(char)

print("?" if len(answer) > 1 else answer[0])
