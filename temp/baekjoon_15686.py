# M 개 골라서 다 해보는거
# 시간초과됨
from itertools import combinations
from collections import deque
import sys
import os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] + '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


def bfs(chicken, home):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    dist = 0

    for h in home:
        queue = deque([h])
        v = [[0]*N for _ in range(N)]
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) in chicken:  # 수정필요
                    dist += v[x][y]+1
                    queue = deque()
                    break
                elif 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                    v[nx][ny] = v[x][y]+1
                    queue.append((nx, ny))

    return dist


N, M = map(int, input().split())
mat = [input().split() for _ in range(N)]


# find 치킨집
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == '2':
            chicken.append((i, j))
        elif mat[i][j] == '1':
            home.append((i, j))
answer = float('inf')

choose_chickens = combinations(chicken, M)

for choose_chicken in choose_chickens:
    answer = min(answer, bfs(choose_chicken, home))
print(answer)
