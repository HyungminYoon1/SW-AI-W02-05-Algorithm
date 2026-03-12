# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

group_list = [[],[]]
group_list.append(['a', 'b', 'c']) #2
group_list.append(['d', 'e', 'f']) #3
group_list.append(['g', 'h', 'i']) #4
group_list.append(['j', 'k', 'l']) #5
group_list.append(['m', 'n', 'o']) #6
group_list.append(['p', 'q', 'r', 's']) #7
group_list.append(['t', 'u', 'v']) #8
group_list.append(['w', 'x', 'y', 'z']) #9

def main(input_number):
    result = []
    current_array = []
    def recursion(n):
        if len(input_number) == len(current_array):
            result.append("".join(current_array))
            return
        
        for i in range(len(group_list[input_number[n]])):
            current_array.append(group_list[input_number[n]][i])
            recursion(n+1)
            current_array.pop()
    recursion(0)
    return result

input_number = list(map(int,list("2227")))
print(main(input_number))


## for 구문 버전

map_char = {2:["a", "b", "c"],
            3:["d", "e", "f"],
            4:["g", "h", "i"],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z']}
input_nums = "234"

cur_arr = map_char[int(input_nums[0])]
new_arr = []
i = 1
while i < len(input_nums):
    for prev in cur_arr:
        for c in map_char[int(input_nums[i])]:
            new_arr.append(prev+c)
    cur_arr = new_arr[:]
    print(cur_arr)
    new_arr = []
    i+=1