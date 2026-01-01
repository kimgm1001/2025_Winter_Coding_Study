def main():

    a = int(input())
    n = 1
    m = 1

    if a == 1:
        print(1)
    else:
        while True:
            n += 1
            if a <= m + 6 * (n - 1):
                print(n)
                break
            else:
                m += 6 * (n - 1)
                continue

if __name__ == '__main__':
    main()