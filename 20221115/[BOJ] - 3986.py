import sys
input = sys.stdin.readline

N = int(input())
word=[] #체크할 단어
cnt = 0 #좋은 단어 갯수

for i in range(N):
    word.append(input().strip())

for i in range(N):
    w = word[i] #체크할 단어
    l = len(w)  #체크할 단어 길이
    stack=[]
    if l%2 == 1:
        continue #홀수면 좋은 단어 X
    for j in range(l):
        if not stack:#비어있으면 append
            stack.append(w[j])
        else:
            if stack[-1] !=w[j]:
                stack.append(w[j])
            else:
                stack.pop()
    if not stack:
        cnt+=1 #스택 비어있으면 카운팅+1
print(cnt)

############################################################3
#https://www.acmicpc.net/problem/3986
#############################################################

############################################################3
#A가 쌍이 아니라 1개만 나오고 B가 나와버리면 결국 A는 B를 건너서 다음 A와 이어진다. 그럼 사이에 낀 B는 다음 B와 짝지어질때 결국 크로스 나기때문에
#A가 나오면 A가 바로 나와줘야함
#홀수여도 안됨
#위 로직을 스택을 이용해서 서로 다르면 append, 같은경우 pop해준다
#마지막에 스택이 비어있으면 좋은단어
#############################################################