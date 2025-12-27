def main():
    
    import sys
    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        a , b = map(int,input().split())
        print(a+b)


    
if __name__ == '__main__':
    main()