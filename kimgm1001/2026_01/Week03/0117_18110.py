def main():

    import sys

    input = sys.stdin.readline

    def qksdhffla(n):
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

    arr = arr[m : -m]

    print(qksdhffla(sum(arr) / (n - 2 * m)))

if __name__ == '__main__':
    main()