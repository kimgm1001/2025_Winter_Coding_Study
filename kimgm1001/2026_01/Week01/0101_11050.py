def main():

    n, k = map(int, input().split())

    if k == 0:
        print(1)
    elif k == 1:
        print(n)
    else:
        res1 = 1
        res2 = 1

        for i in range(k):
            res1 *= n
            n -= 1

        for i in range(2, k + 1):
            res2 *= i

        print(int(res1 / res2))

if __name__ == '__main__':
    main()