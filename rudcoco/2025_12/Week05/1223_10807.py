def main():
    n = int(input())
    a = list(map(int, input().split()))
    v = int(input())

    number = 0
    for i in a:
        if i == v:
            number += 1
    print(number)
if __name__ == '__main__':
    main()