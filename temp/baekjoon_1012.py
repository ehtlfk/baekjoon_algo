import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# DFS 컴포넌트 개수
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(i,j):
    v[i][j] = 1
    for k in range(4):
        nx = dx[k]+i
        ny = dy[k]+j
        if 0<=nx<N and 0<=ny<M and v[nx][ny] == 0 and baechu[nx][ny] == 1:
            dfs(nx,ny)

for _ in range(int(input())):
    M,N,K = map(int,input().split())
    baechu = [ [0]*(M) for _ in range(N)]
    for _ in range(K):
        s,f = map(int,input().split())
        baechu[f][s] = 1
    v = [[0]*M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and baechu[i][j] == 1:
                dfs(i,j)
                ans +=1
    print(ans)



