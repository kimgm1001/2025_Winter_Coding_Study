def main():

    n = int(input())
    a = list(map(int,input().split()))
    v = int(input())
    c = 0

    for i in a:
        if i == v :
            c += 1
    
    print(c)
    
if __name__ == '__main__':
    main()