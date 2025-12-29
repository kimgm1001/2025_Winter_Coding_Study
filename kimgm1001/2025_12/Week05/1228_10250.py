def main():

    t = int(input())

    for _ in range(t):
        h, w, n = map(int, input().split())

        if n % h == 0:
            a = h
            b = n // h
        else:
            a = n % h
            b = n // h + 1

        print(f"{a}{b:02d}")

if __name__ == '__main__':
    main()