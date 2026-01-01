def main():

    n = int(input())
    arr = list(map(int, input().split()))
    count = 0

    for i in arr:
        if i < 2:
            count += 1
            continue
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    count += 1
                    break
                else:
                    continue

    print(n - count)

if __name__ == '__main__':
    main()