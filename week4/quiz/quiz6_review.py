# 문제

'''
. 아래 깊이 우선 탐색(DFS)의 예시를 참고하여 간선 방문 결과와 비트리(non-tree) 간선 목록을 리턴하는 파이썬 함수를 작성하려고 한다. 아래 빈 곳을 채워 파이썬 함수를 완성하시오. 참고로 각 빈 코드는 한줄 이상의 다중 코드가 될 수 있다. 비트리 간선(non-tree edge)이란 트리 간선이 아닌 나머지 모든 간선(이미 어떤 방식으로든 방문/발견된 정점으로 가는 간선)을 의미한다. 

# 예시

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'G': ['H'],
    'H': ['F'],
  }

def dfs(graph, start):

    visited = []
    back_edges = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            1) __________________________
        else:
            2) __________________________-

    return visited, sorted(list(back_edges))

'''

# 올바른 답안

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'G': ['H'],
    'H': ['F'],
  }

def dfs(graph, start):

    visited = []
    back_edges = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for next_node in reversed(graph[node]):
                if next_node not in visited:
                    stack.append(next_node)
                else:
                    back_edges.add((node, next_node))
        else:
            pass
                    
    return visited, sorted(list(back_edges))