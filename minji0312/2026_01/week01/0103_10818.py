def main():
    N=int(input())
    nums=list(map(int, input().split()))

    max=max(nums)
    min=min(nums)

    print(min, max)

if __name__ == '__main__':
    main()