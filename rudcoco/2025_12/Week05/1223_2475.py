def main():
    a, b, c, d, e = map(int, input().split())
    A = a * a
    B = b * b
    C = c * c
    D = d * d
    E = e * e
    sum = A + B + C + D + E
    vudrbs = sum % 10
    print(vudrbs)
if __name__ == '__main__':
    main()