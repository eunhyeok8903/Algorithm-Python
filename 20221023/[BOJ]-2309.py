li=[] #입력받을 난쟁이 리스트

#입력
for i in range(9):
    li.append(int(input()))

li.sort() #정렬 하고 시작
sum = sum(li) # 난쟁이 키 총합

for i in range(0,9):
    for j in range(i+1,9):
        if (sum-li[i]-li[j]) == 100:
            #2명을 뺀 7명의 난쟁이 키의 합이 100일때 2명 빼고 모두 출력
            for k in range(0,9):
                if k==i or k==j :
                    continue
                else:
                    print(li[k])
            exit()