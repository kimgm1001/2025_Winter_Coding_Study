def main():
    
    n,x = map(int,input().split())
    a = list(map(int, input().split()))
    for k in a:
        if k < x:
            print(k, end = " ")

            

if __name__ == '__main__':
    main()