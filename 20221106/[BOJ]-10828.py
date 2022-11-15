import sys
input = sys.stdin.readline #readline을 input처럼 사용가능
N = int(input())
li=[]

for i in range(N):
    command = list(input().split())
    if command[0] =="pop":
        if len(li)==0:
            print(-1)
        else:
            print(li.pop())
    elif command[0] =="size":
        print(len(li))
    elif command[0] =="empty":
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif command[0] =="top":
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])
    else:
        li.append(int(command[1]))



