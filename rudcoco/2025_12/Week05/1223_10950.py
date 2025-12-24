def main():
    a = int(input())
    for _ in range(a):
        b, c = map(int, input().split())
        print(b + c)

if __name__ == '__main__':
    main()