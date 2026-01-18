import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    w = input()
    c1 = 0
    c2 = 0

    for i in w:
        if i == '(':
            c1 += 1
        elif i == ')':
            c2 += 1
        if c2 > c1:
            print('NO')
            break
    else:
        if c1 == c2:
            print('YES')
        else:
            print('NO')