def main():
    N=int(input())
    x=1
    if N==0:
        print(1)
    else:
        for i in range(N):
            x=x*(i+1)
        print(x)

if __name__ == '__main__':
    main()