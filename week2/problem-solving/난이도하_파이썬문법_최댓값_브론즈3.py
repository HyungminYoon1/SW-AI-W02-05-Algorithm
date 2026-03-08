# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


def get_number_input():
    nums = []
    for i in range(9):
        input_number = int(input())
        nums.append(input_number)
    return nums

def print_max_num(nums):
    
    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num
    
    location = nums.index(max_num)+1

    print(max_num)
    print(location)

def main():
    nums = get_number_input()
    print_max_num(nums)

if __name__ == "__main__":
    main()


## gpt 코칭 후 개선한 코드
''' 

nums = [int(input()) for _ in range(9)]

max_num = max(nums)
location = nums.index(max_num) + 1

print(max_num)
print(location)

'''
    
    
    

    

