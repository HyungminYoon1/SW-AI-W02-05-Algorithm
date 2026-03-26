# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

'''
풀이 전략
이 문제는 TrieNode를 하나 만들고, Trie는 그 루트 노드만 들고 있다고 생각하면 단순화 가능합니다.

1. 각 노드는 2가지만 가짐
- children: 다음 문자로 가는 자식들
- is_end: 여기서 단어가 끝나는지 표시하는 값

2. children은 파이썬에서 보통 2가지 방식이 있습니다.
- 쉬운 방식: dict
- 빠르고 정석 느낌: 길이 26짜리 리스트

3. insert(word)
- 루트부터 시작
- 글자를 하나씩 보면서
- 없으면 새 노드 생성
- 있으면 그 노드로 이동
- 마지막 글자에 도착하면 is_end = True

4. search(word)
- 루트부터 글자를 따라가다가 중간에 없으면 False
- 끝까지 갔더라도 is_end가 True일 때만 True
*즉, "apple"만 넣었으면 "app"는 False
'''

'''
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
'''

# TrieNode: 한 글자를 기준으로 다음 글자들로 뻗어나가는 노드
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    # word를 삽입
    def insert(self, word: str) -> None:

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # (클래스 내부에서만 사용하는 보조함수) 경로를 따라가서 마지막 노드를 반환하는 함수
    def _find(self, prefix):

        node = self.root
        
        for ch in prefix: # 문자열이나 접두사를 따라가다가:
            if ch not in node.children: # 중간에 없으면 None 반환
                return None
            node = node.children[ch]
        return node # 끝까지 찾으면 마지막 노드 반환

    # 문자열이 트리에 있을 때(즉, 먼저 삽입되었을 때) True, 그렇지 않으면 False 반환
    def search(self, word: str) -> bool:

        node = self._find(word) # 단어 끝 노드 찾기

        if node is None:
            return False
        
        return node.is_end # is_end가 False면 경로만 있고 단어는 아님. is_end가 True면 정확히 존재하는 단어

    # 이 접두사로 시작하는 단어가 하나라도 있는지 확인. search()와 차이점은 마지막에 is_end를 보지 않는다
    def startsWith(self, prefix: str) -> bool:
        
        node = self._find(prefix)

        if node is None:
            return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
시간복잡도
insert(word) = O(len(word))
search(word) = O(len(word))
startsWith(prefix) = O(len(prefix))
'''