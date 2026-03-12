# https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

def pow(x, n):

    if n == 0:
        return 1
    
    elif n > 0:
        result = 1
        for _ in range(n):
            result *= x
        return result
    
    else:
        result = 1
        for _ in range(-n):
            result /= x
        return result

# test
print(pow(1.06, -12))
