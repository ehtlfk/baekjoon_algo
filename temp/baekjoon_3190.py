import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input())
K = int(input())

pan = [[0]*N for _ in range(N)]

for _ in range(K):
    x,y = map(int,input().split())
    pan[x-1][y-1] = 1

L = int(input())
moves = [input().strip().split() for _ in range(L)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

t = 0
if moves:
    X, C = moves.pop(0)
    i = int(X)
d = 0
hx = 0
hy = 0
tx = 0
ty = 0
pan[hx][hy] = 9
q = [(tx,ty)]


while True:
    t+=1
    hx += dx[d]
    hy += dy[d]
    
    if not (0<=hx<N and 0<=hy<N) or pan[hx][hy] == 9:
        break
    
    if pan[hx][hy] != 1: # 뱀이 겹치면서 갈 수 있음
        tx,ty = q[0]
        pan[tx][ty] = 0
        q.pop(0)
    q.append((hx,hy))
    pan[hx][hy] = 9

    if t == i:
        if C == 'L':
            d = (d+1)%4
        elif C == 'D':
            d = (d-1)%4
        if moves:
            X, C = moves.pop(0)
            i = int(X)

print(t)