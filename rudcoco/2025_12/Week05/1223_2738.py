def main():
    n, m = map(int, input().split())

    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            print(a[i][j] + b[i][j], end = ' ')
        print()
if __name__ == '__main__':
    main()