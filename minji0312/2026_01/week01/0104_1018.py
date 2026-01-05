def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    N, M = map(int, input().split())
    board=[input().rstrip() for _ in range(N)]
    result=[]

    for i in range(N-7):
        for k in range(M-7):
            count_W=0
            count_B=0

            for a in range(i,i+8):
                for b in range(k,k+8):
                    if (a+b)%2==0:
                        if board[a][b]!="W":
                            count_W+=1
                        if board[a][b]!="B":
                            count_B+=1
                    else:
                        if board[a][b]!="B":
                            count_W+=1
                        if board[a][b]!="W":
                            count_B+=1

            result.append(count_W)
            result.append(count_B)

    print(min(result))

if __name__ == '__main__':
    main()