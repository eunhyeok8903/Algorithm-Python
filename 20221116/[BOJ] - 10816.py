import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().rstrip().split()))
card.sort()

print(card)
M = int(input())
number = list(map(int,input().rstrip().split()))
dic={}
for i in range(len(card)):
    if card[i] in dic:
        dic[card[i]]+=1
    else:
        dic[card[i]]=1
#print(dic)

result = []
for j in range(len(number)):
    if number[j] in dic:
        result.append(dic[number[j]])
    else:
        result.append(0)
print(' '.join(list(map(str,result))))

############################################################3
#https://www.acmicpc.net/problem/10816
#############################################################


