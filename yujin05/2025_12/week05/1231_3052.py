def main():

    l = []

    for i in range(10):
        n = int(input())
        rest = n % 42
        l.append(rest)

    if len(l) != len(set(l)):
        print(len(set(l)))
    else:
        print(len(l))

if __name__ == '__main__':
    main()

# set 중복요소 있을 경우 활용 