def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    while True:
        num=list(map(int, input()))
        if num[0]==0:
            break
        else:
            if num==list(reversed(num)):
                print("yes")
            else:
                print("no")

if __name__ == '__main__':
    main()