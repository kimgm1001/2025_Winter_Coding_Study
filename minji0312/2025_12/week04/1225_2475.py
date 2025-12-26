def main():
    def BaekJoon2(list):
        sum=0
    for i in list:
        sum=sum+i**2
    r=sum%10
    print(r)

    num=list(map(int, input().split()))
    BaekJoon2(num)

if __name__ == '__main__':
    main()