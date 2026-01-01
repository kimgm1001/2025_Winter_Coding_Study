def main():

    n = int(input())
    arr = list(map(int, input().split()))
    t, p = map(int, input().split())
    r1 = 0

    for i in arr:
        if i % t == 0:
            r1 += i // t
        else:
            r1 += (i // t) + 1

    r2_1 = n // p
    r2_2 = n % p

    print(r1)
    print(f'{r2_1} {r2_2}')

if __name__ == '__main__':
    main()