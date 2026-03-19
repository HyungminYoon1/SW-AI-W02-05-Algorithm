'''
6. 다음은 정렬된 정수 배열 arr에서 target 값을 찾아 인덱스를 반환하는 이진 탐색 알고리즘이다. 아래 코드의 빈칸에 들어갈 알맞은 내용을 채우시오. 
(단, target이 존재하지 않으면 -1을 반환해야 한다.)

def binary_search(arr, target):

    left = 0
    right = __________ (1)       

    while left <= right:         

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = __________ (2) 
        else:
            right = __________ (3) 

    return -1
'''

def binary_search(arr, target):

    left = 0
    right = len(arr)

    while left <= right:         

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

'''
# 작성한 응답
(1) len(arr)
(2) mid + 1
(3) mid - 1
'''

'''
올바른 답
(1) len(arr) - 1
(2) mid + 1
(3) mid - 1
'''