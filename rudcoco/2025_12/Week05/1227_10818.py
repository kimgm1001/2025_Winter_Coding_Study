def main():
    a = int(input())
    b = list(map(int, input().split()))
    mini = min(b)
    maxx = max(b)

    print(mini, maxx)
if __name__ == '__main__':
    main()