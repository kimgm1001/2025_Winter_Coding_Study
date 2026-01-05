def main():
    N=int(input())
    num=list(map(int,input()))
    count=0
    for i in num:
        count+=i
    print(count)

if __name__ == '__main__':
    main()