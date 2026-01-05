def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    N=int(input())
    score=list(map(int, input().split()))

    M=max(score)
    new=[]
    for i in score:
        n=i/M*100
        new.append(n)

    total=0
    for i in new:
        total+=i

    print(total/N)

if __name__ == '__main__':
    main()