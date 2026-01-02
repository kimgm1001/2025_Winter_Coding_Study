def main():
    n = []
    skajwl = []
    for _ in range(10):
        a = int(input())
        n.append(a)
    for i in n:
        b = i % 42
        if b not in skajwl:
            skajwl.append(b)
    print(len(skajwl))

if __name__ == '__main__':
    main()