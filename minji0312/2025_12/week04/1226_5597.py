def main():
    num=[i for i in range(1,31)]
    for k in range(28):
        n=int(input())
        num.remove(n)
    print(num[0])
    print(num[1])

if __name__ == '__main__':
    main()