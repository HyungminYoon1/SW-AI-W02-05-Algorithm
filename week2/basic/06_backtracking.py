"""
[백트랙킹 - 조합 생성]

문제 설명:
- n개의 숫자 중에서 k개를 선택하는 모든 조합을 찾습니다.
- 백트랙킹을 사용하여 가능한 모든 조합을 탐색합니다.
- 조합은 순서가 없으므로 [1,2]와 [2,1]은 같은 조합입니다.

입력:
- n: 전체 숫자의 개수 (1부터 n까지)
- k: 선택할 숫자의 개수

출력:
- 모든 가능한 조합의 리스트

예제:
입력: n = 4, k = 2
출력: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

힌트:
- 백트랙킹의 3단계: 선택(Choose) → 탐색(Explore) → 취소(Unchoose)
- 현재 숫자보다 큰 숫자만 선택하여 중복 방지
"""

def combinations(n, k):
    """
    1부터 n까지 숫자 중 k개를 선택하는 모든 조합 찾기
    
    Args:
        n: 전체 숫자 개수
        k: 선택할 개수
    
    Returns:
        모든 조합의 리스트
    """
    result = []
    
    def backtrack(start, current_combination):
        """
        백트랙킹 헬퍼 함수
        
        Args:
            start: 탐색을 시작할 숫자
            current_combination: 현재까지 선택한 숫자들
        """
        # TODO: base case - k개를 모두 선택했으면 결과에 추가
        if len(current_combination) == k:
            result.append(current_combination.copy()) # k개 조합이 완료되면 그 복사본을 저장한다. 원본을 더할 경우 current_combination 객체의 참조가 저장된다. 백트래킹 과정에서 current_combination이 계속 수정되므로 모든 결과가 동일한 리스트 객체를 가리키게 된다.
            return

        # TODO: start부터 n까지 숫자를 하나씩 시도
        for i in range(start, n+1):
           
            ## TODO: 백트랙킹 3단계 구현
            ## 1. 선택(Choose)
            current_combination.append(i) # 조합 리스트에 숫자를 추가한다
            ## 2. 탐색(Explore)
            backtrack(i+1, current_combination) # 재귀 탐색: 그 다음 단계로 넘어가 조합 리스트에 숫자를 더 추가한다
            ## 3. 선택 취소(Unchoose)
            current_combination.pop() # 리스트의 마지막 요소 제거: 재귀 탐색이 끝나면 현재 선택을 취소하여 이전 상태로 되돌린다. 그래야 다음 후보 숫자 시도가 가능한다.
            # 재귀 호출(backtrack)이 끝나면 항상 pop이 실행된다. 이는 성공 여부와 관계없이 현재 선택을 취소하여 이전 상태로 복귀하기 위함이다.
    
    backtrack(1, [])
    return result

def combinations_itertools_compare(n, k):
    """
    itertools를 사용한 조합 생성 (비교용)
    """
    from itertools import combinations as comb
    return [list(c) for c in comb(range(1, n+1), k)]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()
    
    # 테스트 케이스 3
    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()
    
    # 테스트 케이스 4
    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")