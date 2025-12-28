def main():

    import numpy as np

    n, m = map(int, input().split())
    arr1 = []

    for _ in range(n * 2):
        arr1.append(np.array(list(map(int, input().split()))))

    for i in range(n):
        result = arr1[i] + arr1[i + n]
        print(*result)

if __name__ == '__main__':
    main()