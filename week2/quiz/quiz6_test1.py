'''
6. 한 절에는 여러 명의 스님이 살고 있다. 병에 걸린 스님은 머리에 붉은 점이 생기며, 스님들은 매일 아침 한자리에 모여 서로의 얼굴을 볼 수 있지만 자신의 얼굴은 볼 수 없다. 어느 날 아침, 주지 스님이 모든 스님에게 “이 절에는 머리에 붉은 점이 있는 스님이 최소 한 명 이상 있다”고 말했다. 이 날을 0일차라고 하며, 그 이후로 병에 걸린 스님의 수는 변하지 않는다. 스님들은 매일 아침 서로의 머리를 확인하면서 자신이 병에 걸렸는지 논리적으로 판단한다. 어떤 스님이 자신의 머리에 붉은 점이 있다는 사실을 확실히 알게 되면, 그 스님은 다음 날 아침 모임에 나오지 않고 절을 떠난다. 그런데 1일차부터 6일차 아침까지는 아무도 절을 떠나지 않았다. 그러나 7일차 아침이 되자 머리에 붉은 점이 있던 스님들이 모두 동시에 절을 떠나 더 이상 보이지 않았다. 이때 머리에 붉은 점이 있던 스님은 몇 명이었는가? 또한 붉은 점이 있는 스님이 n명일 때, 모든 스님이 절을 떠나는 날을 반환하는 재귀 함수 departure_day(n)을 작성하라. (단, 주지 스님은 병에 걸리지 않았다.) (2점)
'''

# 가장 단순한 재귀 구조
def departure_day(n):
    if n == 1:
        return 1
    return departure_day(n - 1) + 1

# 사고 과정까지 재귀적으로 출력
def departure_day_with_reason(n: int, depth: int = 0) -> int:
    indent = "    " * depth

    if n <= 0:
        raise ValueError("n은 1 이상의 정수여야 합니다.")

    if n == 1:
        print(f"{indent}붉은 점 스님이 1명인 경우:")
        print(f"{indent}- 그 스님은 다른 누구에게도 붉은 점을 보지 못한다.")
        print(f"{indent}- 그런데 주지 스님이 '최소 1명은 있다'고 말했다.")
        print(f"{indent}- 따라서 자기 머리에 붉은 점이 있음을 안다.")
        print(f"{indent}- 그래서 1일차 아침에 떠난다.")
        return 1

    print(f"{indent}붉은 점 스님이 {n}명인 경우를 생각해보자.")
    print(f"{indent}- 각 붉은 점 스님은 다른 붉은 점 스님 {n-1}명을 본다.")
    print(f"{indent}- 각자는 '혹시 내 머리에는 점이 없고, 실제로는 {n-1}명뿐 아닐까?'라고 가정한다.")
    print(f"{indent}- 그렇다면 그 {n-1}명은 다음과 같이 행동해야 한다:")

    prev_day = departure_day_with_reason(n - 1, depth + 1)

    print(f"{indent}- 만약 실제로 {n-1}명뿐이라면, 그들은 {prev_day}일차 아침에 떠나야 한다.")
    print(f"{indent}- 그런데 {prev_day}일차 아침까지 아무도 떠나지 않았다.")
    print(f"{indent}- 따라서 각 스님은 '내 머리에도 붉은 점이 있구나'라고 결론낸다.")
    print(f"{indent}- 그래서 {prev_day + 1}일차 아침에 모두 떠난다.")

    return prev_day + 1

# 한 스님 기준
def monk_thinking(seen: int, depth: int = 0) -> int:
    indent = "    " * depth

    if seen < 0:
        raise ValueError("seen은 0 이상이어야 합니다.")

    if seen == 0:
        print(f"{indent}나는 다른 누구에게도 붉은 점을 보지 못한다.")
        print(f"{indent}그런데 최소 1명은 있다고 했으니, 그 한 명은 나다.")
        print(f"{indent}따라서 나는 1일차 아침에 떠난다.")
        return 1

    print(f"{indent}나는 다른 스님 {seen}명의 머리에서 붉은 점을 본다.")
    print(f"{indent}혹시 내 머리에는 붉은 점이 없다고 가정해보자.")
    print(f"{indent}그러면 실제 붉은 점 스님 수는 {seen}명이어야 한다.")
    print(f"{indent}그 경우 그들은 언제 떠나야 하는가?")

    assumed_day = monk_thinking(seen - 1, depth + 1)

    print(f"{indent}{seen}명만 있었다면 그들은 {assumed_day + 1 if seen > 0 else 1}일차에 떠나야 한다는 식으로 귀납이 진행된다.")
    actual_day = seen + 1
    print(f"{indent}그런데 그날까지 아무도 떠나지 않았다.")
    print(f"{indent}따라서 내 머리에도 붉은 점이 있다.")
    print(f"{indent}그래서 나는 {actual_day}일차 아침에 떠난다.")

    return actual_day


# 가장 깔끔한 구조: 계산 함수 + 추론 함수 분리

def monk_reasoning(seen_red: int, depth: int = 0) -> int:
    """
    한 스님이 다른 스님들 머리에서 붉은 점을 seen_red명 봤을 때,
    자신이 언제 확신하고 떠나는지 재귀적으로 설명한다.
    """
    indent = "    " * depth

    if seen_red < 0:
        raise ValueError("seen_red는 0 이상이어야 합니다.")

    if seen_red == 0:
        print(f"{indent}[기저 사례]")
        print(f"{indent}나는 아무에게도 붉은 점을 보지 못한다.")
        print(f"{indent}하지만 최소 1명은 있다고 알려졌다.")
        print(f"{indent}그러므로 그 한 명은 나다.")
        print(f"{indent}나는 1일차 아침에 떠난다.")
        return 1

    print(f"{indent}[재귀 사례]")
    print(f"{indent}나는 다른 스님 {seen_red}명의 머리에서 붉은 점을 본다.")
    print(f"{indent}만약 내 머리에 붉은 점이 없다면, 실제 붉은 점 스님은 {seen_red}명뿐이다.")
    print(f"{indent}그 {seen_red}명이 언제 떠나는지 생각해보자.")

    assumed_departure = monk_reasoning(seen_red - 1, depth + 1)

    print(f"{indent}{seen_red}명뿐이었다면, 그들은 {departure_day(seen_red)}일차 아침에 떠나야 한다.")
    print(f"{indent}그런데 그날까지 아무도 떠나지 않았다.")
    print(f"{indent}따라서 내 머리에도 붉은 점이 있다.")
    print(f"{indent}나는 {departure_day(seen_red + 1)}일차 아침에 떠난다.")

    return departure_day(seen_red + 1)


day = monk_reasoning(6)
print("최종 떠나는 날:", day)