def main():

    a, b = map(int, input().split())
    r = 0

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            r = i

    print(r)
    print(int(a * b / r))

if __name__ == '__main__':
    main()