import sys

input = sys.stdin.readline

n = int(input())
temp = 0

while 0 < n - temp:
    if (n - temp) % 5 == 0:
        print(((n - temp) // 5) + (temp // 3))
        exit()
    else:
        temp += 3
        continue

if n % 3 == 0:
    print(n // 3)
else:
    print(-1)