def main():

    import sys

    input = sys.stdin.readline

    def qksdhffla(n):       ## 반올림
        return int(n + 0.5)

    n = int(input())

    if n == 0:
        print(0)
        exit()

    arr = []

    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    m = qksdhffla(n * 0.15)

    # arr = arr[m : -m]     m = 0 인 경우, [0 : 0] 으로 빈 리스트를 output 하게 됨
    arr = arr[m : n - m]

    print(qksdhffla(sum(arr) / (n - 2 * m)))

if __name__ == '__main__':
    main()