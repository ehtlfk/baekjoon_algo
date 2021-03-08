# 룩 2개로 13개 이하 폰 잡아먹기, 폰 다잡을 때까지 룩 최소 이동 거리
N = 3
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# rooks = [[1,0],[3,3]]
# pawns = [[0,3],[1,2],[3,1]]
rooks = [[0,0],[2,2]]
pawns = [[0,1],[0,2]]
chess = [[0]*N for _ in range(N)]
for p in pawns:
    x,y = p
    chess[x][y] = 1
answer = 0

def bfs(rook,p_cnt,chess):
    queue = [rook]
    v = [[0]*N for _ in range(N)]
    cnt =[0]*p_cnt
    chess =[ c[:] for c in chess[:]]
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0<=nx<N and 0<=ny<N and v[nx][ny]==0:
                v[nx][ny] = v[x][y]+1
                queue.append((nx,ny))
                if chess[nx][ny] == 1:
                    p_cnt-=1
                    chess[nx][ny] = 0
                    cnt[p_cnt]=v[nx][ny]
                    v[nx][ny] = 0
                    if p_cnt == 0:
                        return cnt
print(bfs(rooks[0],len(pawns),chess))
print(bfs(rooks[1],len(pawns),chess))