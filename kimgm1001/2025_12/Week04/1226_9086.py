def main():

    n = int(input())

    for _ in range(n):
        w = list(input())
        print(w[0], end="")
        print(w[-1])

if __name__ == '__main__':
    main()