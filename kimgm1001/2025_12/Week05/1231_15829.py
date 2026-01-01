def main():

    n = input()
    w = input()
    res = 0

    for i in range(len(w)):
        res += (ord(w[i]) - 96) * (31 ** i)

    print(res % 1234567891)

if __name__ == '__main__':
    main()