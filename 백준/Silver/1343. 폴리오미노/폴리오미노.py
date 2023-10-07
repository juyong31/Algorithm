# 리스트를 쭉 돌면서 'X'가 4개 연속나오면, 그 4개항목에 대해서 바로 'A'로 변환
# 'X'가 4개 미만으로 나온상태에서 '.'이 나온 경우, 'X'가 2개이면 'B'로 변환 / 그렇지않을 경우(1or3) print(-1)

graph = list(map(str, input()))
cnt = 0

for i in range(len(graph)):
    if(graph[i] == 'X'): #X인 경우
        cnt += 1
        if(cnt == 4): #cnt = 4이면 우선적으로 A로 바꿔주고, cnt = 초기화
            for j in range(i, i-4, -1):
                graph[j] = 'A'
                cnt = 0
        if(i == len(graph)-1): # X가 맨 마지막에 위치해있고, cnt == 4가 아닌경우
            if(cnt == 2):
                for k in range(i, i-2, -1):
                    graph[k] = 'B'
                    cnt = 0
            elif(cnt == 1 or cnt == 3): # 이걸 else로 다 걸어줘버리면 'XXXX'입력시 결과값 정상 출력이 아닌 exit(0)만남
                print(-1)
                exit(0)
                   
    else: #.인 경우
        if(cnt == 2): #.을 만나기 전 X가 2개 연속으로 온 경우
            for j in range(i-1, i-3, -1):
                graph[j] = 'B'
                cnt = 0
        elif(cnt == 1 or cnt == 3): #.을 만나기 전 X가 1개or3개 연속으로 온 경우
            print(-1)
            exit(0)

for v in range(len(graph)):
    print(graph[v], end = '')