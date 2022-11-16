import sys

input = sys.stdin.readline
N = int(input().rstrip())

for _ in range(N):
    stack = []
    flag = True
    ps = input().rstrip()
    #print(ps)
    for j in range(len(ps)):
        #print(stack)
        if ps[j] == '(':
            stack.append('(')
        else: #')'인경우
            if stack :
                stack.pop()
            else:
                flag=False
                break
    if stack :
        flag = False
    if flag==True:
        print('YES')
    else:
        print('NO')

############################################################3
#https://www.acmicpc.net/problem/9012
#############################################################
