def main():
    t = int(input()) 

    for j in range(t):
        x = input().split() 
        r = int(x[0])
        s = x[1]
    
        for i in s:
            print(r*i, end ='')

        print()

if __name__ == '__main__':
    main()

    # 타입이 다른 문자들을 공백기준으로 입력받은 경우 :
    # (split()사용 후 각 타입에 맞추기 / 접근은 인덱스로)
    
    # 문자열은 리스트에 굳이 안넣어도 리스트요소처럼 꺼낼 수 잇음
