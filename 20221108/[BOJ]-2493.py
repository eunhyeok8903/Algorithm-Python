import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int,input().split()))

li=[0]*N
stack=[]
# for i in range(N):
#     t = tower[i]
#     while stack and tower[stack[-1]]<t:
#         stack.pop()
#     if stack:
#         li[i]=stack[-1]+1
#     stack.append(i)
#
#
# print(' '.join(list(map(str,li))))

for i in range(N):
    t = tower[i]
    while stack and stack[-1][0]<t:
        stack.pop()
    if stack:
        li[i]=stack[-1][1]+1
    stack.append((t,i))
print(' '.join(list(map(str,li))))

############################################################3
#https://www.acmicpc.net/problem/2493
#############################################################
