def main():

    t = int(input())

    for _ in range(t):
        k = int(input())
        n = int(input())

        arr = list(i for i in range(1, n + 1))

        for _ in range(k):
            for i in range(1, n):
                arr[i] += arr[i - 1]

        print(arr[n - 1])

if __name__ == '__main__':
    main()