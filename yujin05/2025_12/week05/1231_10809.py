def main():

    al = "abcdefghijklmnopqrstuvwxyz"
    s = input()

    for i in al:
        if i in s:
            print(s.index(i), end=' ')
        else: 
            print(-1, end=' ')

if __name__ == '__main__':
    main()
