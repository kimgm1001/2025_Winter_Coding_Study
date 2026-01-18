import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = deque(range(1, n + 1))

while len(arr) > 1:
    arr.popleft()       ## 왼쪽에서 하나
    arr.rotate(-1)      ## 왼쪽으로 한 칸

print(*arr)