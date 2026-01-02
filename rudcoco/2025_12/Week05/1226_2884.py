def main():
    a, b = map(int, input().split())
    if a != 0 and b - 45 >= 0:
        print(a, b - 45)
    elif a != 0 and b - 45 < 0:
        print(a - 1, b + 15)
    elif a == 0 and b - 45 >= 0:
        print(a, b - 45 )
    else:
        print(a + 23, b + 15)
if __name__ == '__main__':
    main()