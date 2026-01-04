# def main():
#     import sys
#     input=lambda:sys.stdin.readline().rstrip()
#
#     N=int(input())
#     data=[]
#     for i in range(N):
#         info=[]
#         x,y=map(int, input().split())
#         info.append(x)
#         info.append(y)
#         data.append(info)
#
#     result=[]
#     for i in range(len(data)):
#         count=0
#         rank=0
#         for k in range(len(data)):
#             if data[i][0]<data[k][0] and data[i][1]<data[k][1]:
#                 count+=1
#         rank=count+1
#         result.append(rank)
#
#     for i in result:
#         print(i, end=" ")
#
# if __name__ == '__main__':
#     main()



import sys
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
data=[]
for i in range(N):
    info=[]
    x,y=map(int, input().split())
    info.append(x)
    info.append(y)
    data.append(info)


result=[]
for i in range(len(data)):
    count=0 ## 이거 for문 밖에 넣어서 틀림
    rank=0
    for k in range(len(data)):
        my_weight, my_height = data[i]
        other_weight, other_height = data[k]
        if my_weight<other_weight and my_height<other_height:
            count+=1
    rank=count+1
    result.append(rank)

for i in result:
    print(i, end=" ")