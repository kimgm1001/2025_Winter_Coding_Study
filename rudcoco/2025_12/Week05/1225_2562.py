def main():
    l_n = []
    for i in range(9):
        a = int(input())
        l_n.append(a)
    m_b = max(l_n)
    print(m_b)
    for i in range(0,9):
        if l_n[i] == m_b:
            print(i + 1)

if __name__ == '__main__':
    main()