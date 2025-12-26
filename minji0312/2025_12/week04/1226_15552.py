def main():
    import sys
    T=int(sys.stdin.readline())
    for i in range(T):
        A,B=map(int, sys.stdin.readline().split())
        print(A+B)

if __name__ == '__main__':
    main()