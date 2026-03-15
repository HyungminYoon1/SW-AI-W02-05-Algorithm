# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

def make_order(stack = [], text = ""):

    if text[:4] == "push":
        stack.append(int(text.split()[1]))
        return

    elif text == "pop":
        return -1 if not stack else stack.pop()
        
    elif text == "size":
        return len(stack)
    
    elif text == "empty":
        return 0 if stack else 1
            
    elif text == "top":
        return stack[-1] if stack else -1

    return

order_count = int(input())
stack = []
stacked_orders = []
for i in range(order_count):
    stacked_orders.append(make_order(stack, input()))
for i in range(order_count):
    if stacked_orders[i] is not None:
        print(stacked_orders[i])
        

## gpt가 제시한 개선 코드
import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if cmd[:4] == "push":
        stack.append(int(cmd.split()[1]))
    elif cmd == "pop":
        print(stack.pop() if stack else -1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if stack else 1)
    elif cmd == "top":
        print(stack[-1] if stack else -1)


## gpt가 제시한 최적 코드
import sys

input = sys.stdin.readline
stack = []
out = []

n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        out.append(stack.pop() if stack else "-1")
    elif cmd[0] == "size":
        out.append(str(len(stack)))
    elif cmd[0] == "empty":
        out.append("0" if stack else "1")
    elif cmd[0] == "top":
        out.append(stack[-1] if stack else "-1")

sys.stdout.write("\n".join(out))
