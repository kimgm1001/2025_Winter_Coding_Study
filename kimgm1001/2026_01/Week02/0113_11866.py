import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(range(1, n + 1))

res = []

for _ in range(len(arr)):
    res.append(arr.pop(k - 1))
    k += k
    while k > len(arr):
        k -= len(arr)

print(*res)