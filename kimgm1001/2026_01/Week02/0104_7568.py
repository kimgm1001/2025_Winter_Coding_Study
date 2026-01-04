def main():

    n = int(input())
    arr = []

    for _ in range(n):
        size = list(map(int, input().split()))
        arr.append(size)

    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()