li=[] #난쟁이 키 리스트
sum=0 #난쟁이 키 sum값
flag = False #키 100 값 확인 Flag
m,n= 0,0 # 9명중 7명을 뽑아야하는데 제외시킬 2명

#값 입력받기
for i in range(9):
    n = int(input())
    li.append(n)
    sum+=n

# 제외 시킬 난쟁이 i,j값을 브루트 포스로 찾아줌
for i in range(0,9):
    for j in range(i+1,9): #i+1주의
        if flag ==False:
            temp = sum - li[i] -li[j] #총합에서 2명을 뺐을때 값이 100이면 됨
            if temp==100:
                m,n = i,j
                flag=True #찾으면 Flag값 True
                break

result=[] #결과값 출력 리스트 선언
for k in range(9):
    if k!=m and k!=n:
        result.append(li[k])
result.sort() #정렬

#출력
for k in range(7):
    print(result[k])