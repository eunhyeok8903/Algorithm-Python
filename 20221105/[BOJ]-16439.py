N,M= map(int,input().split())
li=[]
for i in range(N):
    l = list(map(int, input().split()))
    li.append(l)

m=0

for i in range(0,M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            ok=0
            for t in range(0,N):
                ok+=max(li[t][i],li[t][j],li[t][k])
            m=max(m,ok)
print(m)

############################################################3
#https://www.acmicpc.net/problem/16439
#############################################################

