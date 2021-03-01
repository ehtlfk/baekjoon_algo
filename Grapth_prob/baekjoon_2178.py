import sys, os
from collections import deque
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 2<=N,M <=100 최소값이면, backtracking해야함, 음. bfs가 빠를거 같은데, dfs도 똑같을 거 같은데 dfs가 구현하기 더 편함, visit행렬에 ++하면 됨
# 대각선 이동 가능? 인접이라고 했으니까 안되겠네

N, M = map(int,input().split())
# input. strip으로 \n 제거
mat = [ list(input().strip()) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
mn = N*M
def dfs(x,y,cnt):
    global mn
    if x == N-1 and y == M-1: # 아 안빼줬다...
        if cnt < mn:
            mn = cnt
        return
    elif cnt > mn:
        return
    else:
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0<=nx<N and 0<=ny<M and mat[nx][ny] == '1' and v[nx][ny] == 0:
                v[nx][ny] = 1
                dfs(nx,ny,cnt+1)
                v[nx][ny] = 0

def bfs(x,y):
    queue= deque([(0,0)])
    while queue:
        # popleft
        x,y = queue.popleft()
        if x == N-1 and y == M-1:
            return v[x][y]+1
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0<=nx<N and 0<=ny<M and mat[nx][ny] == '1' and v[nx][ny] == 0:
                v[nx][ny] = v[x][y]+1
                queue.append((nx,ny))
        



v= [[0]*M for _ in range(N)]
# dfs(0,0,1)
# print(mn)
print(bfs(0,0))

