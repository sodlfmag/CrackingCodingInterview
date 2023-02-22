'''
1.8 0 행렬
M X N 행렬의 한 원소가 0일 경우, 해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.
'''
from pprint import pprint
arr = []
M, N = map(int, input().split())
for i in range(M):
    temp = list(map(int, input()))
    arr.append(temp)

index = []
for i in range(M):
    for j in range(N):
        if(arr[i][j] == 0):
            index.append((i, j))

for i in range(len(index)):
    row = index[i][0]
    col = index[i][1]
    # 세로 0으로 만들기
    for j in range(M):
        arr[j][col] = 0
    # 가로 0으로 만들기
    arr[row] = [0] * N

pprint(arr)

'''
입력
4 5
11111
10111
11011
11111

출력
10011
00000
00000
10011
'''
