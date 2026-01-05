def main():
    music=list(map(int, input().split()))
    alist=[1,2,3,4,5,6,7,8]
    dlist=[8,7,6,5,4,3,2,1]

    if alist==music:
        print("ascending")
    if dlist==music:
        print("descending")
    if music!=alist and music!=dlist:
        print("mixed")

if __name__ == '__main__':
    main()





