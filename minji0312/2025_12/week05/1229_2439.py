def main():
    N = int(input())
    for i in range(N):
        print(" "*(N-(i+1)) + "*"*(i+1))

if __name__ == '__main__':
    main()