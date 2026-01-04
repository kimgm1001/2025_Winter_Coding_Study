def main():

    a = input()
    b = input()
    c = input()

    res = 0

    if a.isdigit():
        res = int(a) + 3
    elif b.isdigit():
        res = int(b) + 2
    elif c.isdigit():
        res = int(c) + 1

    if res % 15 == 0:
        print('FizzBuzz')
    elif res % 3 == 0 and res % 5 != 0:
        print('Fizz')
    elif res % 5 == 0 and res % 3 != 0:
        print('Buzz')
    else:
        print(res)

if __name__ == '__main__':
    main()