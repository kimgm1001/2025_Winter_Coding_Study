def main():
    while True:
        a, b = map(int, input().split())
        if a + b != 0:
            print(a + b)
        else:
            break
if __name__ == '__main__':
    main()