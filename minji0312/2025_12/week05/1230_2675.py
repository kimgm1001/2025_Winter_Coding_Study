def main():
    T=int(input())
    for i in range(T):
        R, S=input().split()
        for k in range(int(R)):
            for l in S:
                print(l, end='')
        print()

if __name__ == '__main__':
    main()