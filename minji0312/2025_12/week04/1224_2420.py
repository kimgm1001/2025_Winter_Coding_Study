def main():
    N,M=map(int, input().split())
    d=N-M
    if d<0:
        print(-d)
    elif d>0:
        print(d)
    else:
        print(0)

if __name__ == '__main__':
    main()