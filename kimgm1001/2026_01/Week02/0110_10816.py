import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
count = Counter(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

for i in target:
    print(count[i], end=' ')