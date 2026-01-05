def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    S=input()
    alphabet="abcdefghijklmnopqrstuvwxyz"

    for i in alphabet:
        print(S.find(i), end=" ")

if __name__ == '__main__':
    main()