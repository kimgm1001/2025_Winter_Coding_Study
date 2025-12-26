import sys
def main():
    a = int(sys.stdin.readline())
    for _ in range(a):
        b, c = map(int, sys.stdin.readline().split())
        print(b + c)
if __name__ == '__main__':
    main()