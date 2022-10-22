
N, M = map(int,input().split())
li = list(map(int, input().split()))
result = 0

for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            temp = li[i]+li[j]+li[k]
            if temp > M:
                continue
            if result<temp:
                result=temp
print(result)




