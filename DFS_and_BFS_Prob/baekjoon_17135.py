import sys, os
from itertools import combinations
from collections import deque
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline
            
# 궁수 모두 동시 공격, 가장가까운, 같으면 왼쪽, 같은 적이 여러 궁수에게 다굴 가능, 적이 성에 도달하면 제외됨 왜?, 궁수의 공격으로 제거할 수 있는 적의 최대수

#거리는 맨해튼
# N,M<=15, D<=10, bfs, 턴마다 진행시키면됨...?, dfs도 되겠는데?
# 문제를 제대로 읽자, 1은 적이 있는 칸이고, 주어진 격자 아래는 전부 성
# def bfs():
#     queue = deque()
#     while queue:
dx = [0,-1,0]
dy = [-1,0,1]
# 아 동시가능이네
# 거리가 D 이내
def bfs(ach):
    cnt = 0
    temp = N
    c_m = [ c[:] for c in m]
    while temp > 0:
        a1,a2,a3 = ach
        achs = [(temp,a1),(temp,a2),(temp,a3)]
        kill = set()
        
        for a in achs:
            queue = deque([a])
            o_x, o_y =a
            flag = 0
            v= [[0]*M for _ in range(N)]
            while queue:
                x,y = queue.popleft()
                if abs(o_x-x)+abs(o_y-y)>=D:
                    break
                for k in range(3):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M and c_m[nx][ny] == 1:
                        kill.add((nx,ny))
                        flag = 1
                        break
                    elif 0<=nx<N and 0<=ny<M and v[nx][ny] == 0:
                        v[nx][ny] = 1
                        queue.append((nx,ny))
                if flag:
                    break
        for k in kill:
            x,y= k
            c_m[x][y] = 0
            cnt += 1
        temp-=1
        for j in range(M):
            c_m[temp][j] = 0
    return cnt
        

N, M, D = map(int,input().split())
m = [ list(map(int,input().split())) for _ in range(N)]
m.append([2]*M)
# 배치하고 돌려야겠네?
# 아쳐를 한 칸 앞으로 이동시키는 거와 같음
achs = list(combinations(range(M),3))
ans =0
for ach in achs:
    cnt = bfs(ach)
    if cnt > ans:
        ans = cnt
print(ans)