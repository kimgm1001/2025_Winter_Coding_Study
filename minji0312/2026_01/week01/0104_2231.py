def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    N=int(input())

    result=[]
    for i in range(1,N):
        nums=list(map(int, str(i)))
        hap=0
        for k in nums:
            hap+=k
        if i+hap==N:
            result.append(i)
    if len(result)==0:
        print(0)
    else:
        print(min(result))

if __name__ == '__main__':
    main()

