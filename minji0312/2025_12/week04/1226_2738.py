def main():
    N,M=map(int, input().split())
    A=[]
    for i in range(N):
        row=list(map(int, input().split()))
        A.append(row)
    B=[]
    for i in range(N):
        row=list(map(int, input().split()))
        B.append(row)

    for k in range(N):
        for i in range(M):
            print(A[k][i]+B[k][i], end=" ")
        print()

if __name__ == '__main__':
    main()