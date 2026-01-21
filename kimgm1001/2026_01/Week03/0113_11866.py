import sys
from collections import deque

def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())

    arr = deque(i for i in range(1, n + 1))

    arr1 = []

    for _ in range(n):
        arr.rotate(-k + 1)
        arr1.append(arr.popleft())

    print(f'<{', '.join(map(str, arr1))}>')

if __name__ == '__main__':
    main()