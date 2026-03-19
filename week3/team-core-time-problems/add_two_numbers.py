# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

text1 = ''
text2 = ''

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

compare_output = [8,9,9,9,0,0,0,1]

while l1:
    text1 += str(l1.pop())

while l2:
    text2 += str(l2.pop())

result_rever_text = int(text1) + int(text2) # 정수
result = str(result_rever_text)[::-1]

print(list(map(int, result)))

