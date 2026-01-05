def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    T=int(input())
    for i in range(T):
        H,W,N = map(int, input().split())
        if H>=N:
            print(str(N)+"01")
        else:
            floor=str(N%H)
            room=str((N//H)+1)
            if int(room)<10:
                room="0"+room

            if int(floor)!=0:
                print(floor+room)
            else:
                room=str(N//H)
                if int(room)<10:
                    room="0"+room
                print(str(H)+room)

if __name__ == '__main__':
    main()