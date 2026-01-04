def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    N, M = map(int, input().split())

    nums=list(map(int, input().split()))

    case=[]
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                hap=nums[i]+nums[j]+nums[k]
                case.append(hap)

    result=[]
    for i in case:
        if i<=M:
            result.append(i)

    print(max(result))

if __name__ == '__main__':
    main()