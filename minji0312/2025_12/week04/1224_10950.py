def main():
    alist=[]
    T=int(input())
    for i in range(T):
        A,B=map(int, input().split())
        hap=A+B
        alist.append(hap)
    for i in alist:
        print(i)

if __name__ == '__main__':
    main()