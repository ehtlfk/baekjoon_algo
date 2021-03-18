import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

from collections import deque
# 자신의 크기보다 작은 처음은 2, 크기가 같으면 먹을 수 는 없는데 지나는 갈 수 있음
# 먹을 수 있는게 없다
# 위쪽 왼쪽 순으로 먹음
# mat 복사해야하니까 deep copy
# 아기 상어는 '자신의 크기'와 같은 수의 물고기를 먹어야 1증가
# 더 이상 먹을 게 없을때
# bfs

# 우선 위치에서 제일 가까운 먹을 수 있는 먹이 탐색, 발견하면 거기로 이동
# 다시 그 위치에서 제일 가까운 거 탐색
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

def bfs(i,j):
    dx = [0,1,0,-1] # 우하좌상, 이걸 조절해도, 안됨, 어느 점의 왼쪽은 어느 저의 위쪽일 수도 있음
    dy = [1,0,-1,0]
    t = 0
    queue = deque([(i,j)])
    size = 2
    cnt = [i for i in range(100)]
    v = [[0]*N for _ in range(N)]
    v[i][j] = 1
    while True:
        l = len(queue)
        
        mn = 1000
        mnx = -1
        mny = -1
        # 최소값 찾기
        for tmp in queue:
            x,y = tmp
            if 0 < mat[x][y] < size:
                if mn > mat[x][y]:
                    mn = mat[x][y]
                    mnx = x
                    mny = y
                elif mn == mat[x][y]:
                    if mnx > x:
                        mnx = x
                        mny = y
                    elif mnx == x:
                        if mny > y:
                            mnx = x
                            mny = y      
        if mn <1000:
            queue = deque([(mnx,mny)])
            l = len(queue)
            feeds[mat[mnx][mny]] -=1
            mat[mnx][mny] = 0
            cnt[size]-=1
            if cnt[size] == 0:
                size+=1
            v = [[0]*N for _ in range(N)]
            v[mnx][mny] = 1

        if l == 0 or sum(feeds[:size]) == 0:

            return t
        # 갈 수 있는 경로 찾기
        for _ in range(l):
            x,y = queue.popleft()
            for k in range(4):
                nx = dx[k]+x
                ny = dy[k]+y
                if 0<=nx<N and 0<=ny<N and mat[nx][ny] <= size and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    queue.append((nx,ny))
        t+=1
        
    
bs = tuple()
feeds = [0]*7 
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            bs = (i,j)
            mat[i][j] = 0
        elif mat[i][j]:
            feeds[mat[i][j]]+=1

print(bfs(*bs))