import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    w = input().split()

    if w[0] == 'push':
        stack.append(w[1])

    elif w[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif w[0] == 'size':
        print(len(stack))

    elif w[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif w[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])