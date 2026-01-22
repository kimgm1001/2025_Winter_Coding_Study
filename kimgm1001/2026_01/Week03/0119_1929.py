## 에라토스테네스의 체: 소수만 걸러낼 때 효율적인 방법
## pop: 빼내고, 한 칸씩 값을 옮겨가는 과정 필요 - O(N)
## Boolean: 그냥 값만 덮어씌우기 - O(1)

import sys

def main():
    input = sys.stdin.readline

    m, n = map(int, input().split())

    arr = [False, False] + [True] * (n - 1)

    for temp in range(2, int(n**0.5) + 1):
        if arr[temp] == True:
            for j in range(temp * 2, n + 1, temp):
                arr[j] = False

    for i in range(m, n + 1):
        if arr[i] == True:
            print(i)

if __name__ == '__main__':
    main()
## 풀이가 존나 높다..