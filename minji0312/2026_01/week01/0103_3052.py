def main():
    nums=[]
    for i in range(10):
        n=int(input())
        nums.append(n)

    rest=[]
    for i in nums:
        r=i%42
        rest.append(r)

    print(len(set(rest)))

if __name__ == '__main__':
    main()