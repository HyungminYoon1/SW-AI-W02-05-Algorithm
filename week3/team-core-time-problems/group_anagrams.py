# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

'''
입력: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

출력: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = sorted(strs)
sorted_str = []

for str in strs:
    sorted_str.append(''.join(sorted(str)))

outer_list = []

# 딕셔너리 안에 그룹화
str_dict = {}
for idx, str in enumerate(sorted_str):
    str_dict.setdefault(str, []).append(strs[idx])

# 딕셔너리를 리스트로 파싱해서 길이 순으로 정렬
result = list(str_dict.values())
result.sort(key= len)
print(result)



'''
{  
    "a" : 1,
    "b" : 1,
    "t" : 1
}
'''
# 문자열 -> 딕셔너리로 변환하는 함수


# 딕셔너리끼리 같은지 비교하는 함수