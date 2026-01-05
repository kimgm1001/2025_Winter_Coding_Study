def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    A=int(input())
    B=int(input())
    C=int(input())
    result=str(A*B*C)

    for i in range(10):
        print(result.count(str(i)))

if __name__ == '__main__':
    main()