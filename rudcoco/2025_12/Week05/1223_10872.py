def main():
    a = int(input())

    t = 1
    for i in range(a, 0, -1):
        t *= i
    print(t)
if __name__ == '__main__':
    main()