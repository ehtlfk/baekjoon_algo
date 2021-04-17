import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N, M = map(int,input().split(" "))
mat = [list(input()) for _ in range(N)]

def bfs(red):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    red.append(0)
    queue = [red]

    # v = [[0]*M for _ in range(N)]
    
    while queue:
        tmp = queue.pop(0)
        rx, ry, bx, by,cnt = tmp
        if cnt >= 10 :
            return -1
        for k in range(4):
            nrx = rx + dx[k]
            nry = ry + dy[k]

            nbx = bx + dx[k]
            nby = by + dy[k]

            while mat[nrx][nry] == '.':
                # v[nrx][nry] = v[rx][ry]+1
                nrx += dx[k]
                nry += dy[k]

            while mat[nbx][nby] == '.':
                nbx += dx[k]
                nby += dy[k]

            if mat[nbx][nby] == 'O':
                continue

            if mat[nrx][nry] == 'O':
                return cnt+1


            if nrx == nbx and nry == nby:
                if k==0:
                    if ry > by:
                        nry-= dy[k]
                    else:
                        nby-= dy[k]
                elif k == 1:
                    if ry > by:
                        nby-= dy[k]
                    else:
                        nry-= dy[k]
                elif k == 2:
                    if rx > bx:
                        nrx -= dx[k]
                    else:
                        nbx -= dx[k]
                elif k == 3:
                    if rx > bx:
                        nbx -= dx[k]
                    else:
                        nrx -= dx[k]
            if not( nrx-dx[k]==rx and nry-dy[k]==ry and nbx-dx[k] == bx and nby-dy[k] == by):
                queue.append([nrx-dx[k],nry-dy[k],nbx-dx[k],nby-dy[k],cnt+1])
    return -1
red = [0,0]
blue = [0,0]

for i in range(N):
    for j in range(M):
        if mat[i][j] == 'R':
            red = [i,j]
            mat[i][j] = '.'
        elif mat[i][j] == 'B':
            blue = [i,j]
            mat[i][j] = '.'
red.extend(blue)
print(bfs(red))
# if answer > 10:
#     print(-1)
# else:
#     print(answer)

