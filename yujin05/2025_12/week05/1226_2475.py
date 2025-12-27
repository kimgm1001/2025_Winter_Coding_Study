def main():

    n = list( map(int,input().split()))
    def ver(n) :
        last = sum(i*i for i in n)%10
        return last
    print(ver(n))

if __name__ == '__main__':
    main()