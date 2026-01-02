def main():
    t = int(input())
    for _ in range(t):
        num, rep = input().split()
        num = int(num)
        for i in range(len(rep)):
            print(rep[i] * num, end = '')
        print()
if __name__ == '__main__':
    main()
