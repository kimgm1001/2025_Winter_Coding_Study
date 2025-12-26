def main():
    N=int(input())
    A=list(map(int, input().split()))
    v=int(input())
    count=0
    for i in A:
        if i==v:
            count+=1
    print(count)

if __name__ == '__main__':
    main()