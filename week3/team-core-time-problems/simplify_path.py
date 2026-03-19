# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

'''
기본: /
.: 현재 폴더(아무 효과 없음) 무시
..: 뒤로 한 칸 pop()
...: 그대로 넣기 append(...)
....: 그대로 넣기 append(....)
/: append(/)
// : append(/)
/// : append(/)
/* n : append(/)
그 외 문자(str): append(str)

'''

def simplifyPath(path):

    raw_path = path.split('/')
    new_path = []
    for x in raw_path:
        if x == '':
            continue
        if x == '.':
            continue
        if x == '..' or x == '.. ':
            if len(new_path) > 0:
                new_path.pop()
        else:
            new_path.append(x)

    result = '/' + '/'.join(new_path)

    return result

path1 = "/home/"
path2 = "/home//foo/"
path3 = "/home/user/Documents/.. /사진들"
path4 = "/.. /"

print(simplifyPath(path1))
print(simplifyPath(path2))
print(simplifyPath(path3))
print(simplifyPath(path4))