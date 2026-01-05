def main():
    import sys
    n = int(sys.stdin.readline())
    lst = [0]*10001
    for i in range(n):
        num = int(sys.stdin.readline())
        lst[num] += 1

    for j in range(10001):
        if lst[j] != 0:
            for i in range(lst[j]):
                print(j)

if __name__ == '__main__':
    main()