def main():
    nums=[]
    for i in range(9):
        n=int(input())
        nums.append(n)

    max=nums[0]
    order=1

    for i in range(9):
        if max<nums[i]:
            max=nums[i]
            order=i+1

    print(max)
    print(order)

if __name__ == '__main__':
    main()