def main():
    eksdj = input()
    eng = 'abcdefghijklmnopqrstuvwxyz'
    for i in eng:
        if i in eksdj:
            print(eksdj.index(i), end = ' ')
        else:
            print(-1, end = ' ')

if __name__ == '__main__':
    main()