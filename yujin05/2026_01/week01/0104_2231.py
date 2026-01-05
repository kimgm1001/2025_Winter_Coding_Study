def main():

    n = int(input())
    r = 0

    for i in range(1,n+1):
        num = list(map(int,str(i)))
        m = i + sum(num)

        if m == n:
            r = i
            break
        
    print(r)


if __name__ == '__main__':
    main()