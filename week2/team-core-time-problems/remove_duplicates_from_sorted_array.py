# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [10, 3, 7, 66, 12, 2, 6, 66, 6, 1, 9]
new_nums = []

# nums 의 원소를 하나씩 검사
for num in nums:
    
    ## new_nums 가 비어있으면 new_nums에 num을 넣는다.
    if new_nums == []:
        new_nums.insert(0, num)
    
    ## 비어있지 않을 경우
    else:
        insert_index = 0  # insert_index는 new_nums 에서 num 의 위치를 지정하기 위한 변수
        is_append = False # 맨 뒤에 붙일지 여부를 결정한다

        # num 을 new_nums에 존재하는 첫번째 원소부터 하나씩 비교한다.
        for new_num in new_nums:
            # num 이 new_num보다 작으면, new_num 앞에 넣는다.
            if num < new_num:
                print(num)
                new_nums.insert(insert_index, num)
                is_append = False
                break
            
            # num 이 new_num과 같으면, 해당 시퀀스를 넘기고 그냥 탈출한다.
            if num == new_num:
                print(num)
                is_append = False
                break
             
            # num이 new_nums의 모든 수보다 클 경우 그 수를 new_nums의 맨 뒤에 넣는 로직
            is_append = True
            
            # new_nums 에서 num 의 위치를 그 다음부터 고려한다
            insert_index = insert_index + 1   
        
        if is_append:
            new_nums.append(num)

print(len(new_nums), new_nums)
print(len(sorted(set(nums))), sorted(set(nums))) # 정답 검증용
