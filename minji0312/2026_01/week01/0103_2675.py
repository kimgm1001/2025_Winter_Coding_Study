def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    T=int(input())
    for i in range(T):
        R, S = input().split()
        for i in S:
            print(i*int(R), end="")
        print()

if __name__ == '__main__':
    main()