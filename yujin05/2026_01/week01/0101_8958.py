def main():

    t = int(input())

    for i in range(t):
        p = input()
        count = 0
        total = 0

        for j in range(len(p)):

            if p[j] == 'O' and p[j -1]!= 'X' :
                count += 1
                total += count
            elif p[j] == 'O' and p[j -1] == 'X':
                count = 1
                total += count
            else:
                count = 0

        print(total)

if __name__ == '__main__':
    main()