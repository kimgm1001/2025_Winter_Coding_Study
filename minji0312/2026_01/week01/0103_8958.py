def main():
    import sys
    input=lambda:sys.stdin.readline().rstrip()

    num=int(input())

    for i in range(num):
        answer=input()
        score=0
        count=0

        for k in answer:
            if k=="O":
                count+=1
                score+=count
            else:
                count=0

        print(score)

if __name__ == '__main__':
    main()

