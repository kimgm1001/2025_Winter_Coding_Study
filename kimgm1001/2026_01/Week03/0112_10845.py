import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    w = input().split()

    if w[0] == 'push':
        queue.append(w[1])
    elif w[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif w[0] == 'size':
        print(len(queue))
    elif w[0] == 'empty':
        print(0 if queue else 1)
    elif w[0] == 'front':
        print(queue[0] if queue else -1)
    elif w[0] == 'back':
        print(queue[-1] if queue else -1)