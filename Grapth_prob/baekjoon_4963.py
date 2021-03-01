import sys, os
from collections import deque
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# w,h<=50 dfs같은데, 2500개면 할만하지, 되돌아가는게 아니니까, 아. recursion 1000초과..., bfs 도 됨, 이문제의 근본은 visited 배열을 채우는 거임, 근왜 시간초과?
dx = [0,0,-1,1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def dfs(x,y):
    v[x][y] = 1
    for k in range(8):
        nx = dx[k]+x
        ny = dy[k]+y
        if 0<=nx<H and 0<=ny<W and mat[nx][ny] == 1 and v[nx][ny] == 0:
            dfs(nx,ny)

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        v[x][y] = 1
        for k in range(8):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0<=nx<H and 0<=ny<W and mat[nx][ny] == 1 and v[nx][ny] == 0:
                queue.append((nx,ny))

while True:
    W, H = map(int, input().split())
    if W == 0 and H ==0:
        break
    mat = [ list(map(int, input().split())) for _ in range(H)]
    v = [[0]*W for _ in range(H)]
    cnt =0
    for i in range(H):
        for j in range(W):
            if mat[i][j] == 1 and v[i][j] == 0 :
                bfs(i,j)
                cnt+=1
    print(cnt)

