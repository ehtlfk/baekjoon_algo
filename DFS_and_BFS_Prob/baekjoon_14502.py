import sys, os
from itertools import combinations

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N, M = map(int, input().split(' '))

lab = [ list(map(int, input().split(' '))) for _ in range(N) ]


def bfs(virus,lab):
    dx = [0,0,1, -1]
    dy = [1,-1,0,0]
    total = len(empty)-3
    queue = virus[:]
    # 2차원 배열 deep copy
    
    while queue:
        x,y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx,ny))  
                total-=1
    return total


# 먼저 바이러스의 위치들을 저장 2<=virus<=10
virus = []
empty = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i,j))
        elif lab[i][j] == 0:
            empty.append((i,j))
# 조합 만들기



comb = combinations(empty, 3)
mx = 0
if comb:
    for c in comb:
        c_lab = [ line[:] for line in lab ]
        for i in c:
            x,y = i
            c_lab[x][y] = 1
        num = bfs(virus,c_lab)
        if num> mx:
            mx= num
    print(mx)
else:
    # combinations에서 길이보다 큰 걸 뽑으려 하면 빈 행렬
    print(len(empty))
