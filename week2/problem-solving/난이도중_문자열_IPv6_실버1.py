# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

def decoding_ipv6(original_text):

    # :: 는 최대 한 번만 허용
    if original_text.count("::") > 1:
        raise ValueError("Invalid IPv6 format - too many ::")
    
    def normalize(group):
        if len(group) == 0:
            return group
        if len(group) > 4:
            raise ValueError("Invalid IPv6 format - block too long")
        # 16진수 검사
        int(group, 16)
        return group.zfill(4)
    
    # :: 가 있는 경우
    if "::" in original_text:
        left, right = original_text.split("::")

        left_parts = left.split(":") if left else []
        right_parts = right.split(":") if right else []

        left_parts = [normalize(part) for part in left_parts]
        right_parts = [normalize(part) for part in right_parts]

        missing = 8 - (len(left_parts) + len(right_parts))
        if missing < 1:
            raise ValueError("Invalid IPv6 format - invalid compressed form")

        result = left_parts + ["0000"] * missing + right_parts

    # :: 가 없는 경우
    else:
        parts = original_text.split(":")
        if len(parts) != 8:
            raise ValueError("Invalid IPv6 format - must have 8 groups")
        result = [normalize(part) for part in parts]
    
    if len(result) != 8:
        raise ValueError("Invalid IPv6 format - final group count is not 8")

    return ":".join(result)

input_text = input()
print(decoding_ipv6(input_text))