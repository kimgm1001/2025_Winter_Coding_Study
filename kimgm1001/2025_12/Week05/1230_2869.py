def main():

    a, b, v = map(int, input().split())

    v = v - b

    res = v // (a - b)

    if v % (a - b) != 0:
        res += 1

    print(res)

if __name__ == '__main__':
    main()