# M 개 골라서 다 해보는거
# 시간초과됨
# M개를 골라서 각자의 최소 거리를 찾아 가는 방식으로 하면 너무 오래걸림
# 집의 개수는 2N개를 넘지 못하고 치킨집도 13개 미만이므로 26*50 =1300 개의 경우로 각 집에서 모든 치킨집에 대한 거리를 구함
# 이제 M개를 선택하고 이 M개 중에서 제일 작은 값을 더한 것들의 합중 제일 작은 것이 답

# 모든 치킨 집의 거리를 왜 bfs 로 구함 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 그냥 맨해튼 거리 구하면 되는데
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
    distance = [{d: 0 for d in chicken} for _ in range(len(home))]

    for i in range(len(home)):
        queue = deque([home[i]])
        v = [[0]*N for _ in range(N)]
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                # 수정필요
                if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0:
                    if mat[nx][ny] == '2':
                        distance[i][(nx, ny)] = v[x][y]+1
                    v[nx][ny] = v[x][y]+1
                    queue.append((nx, ny))

    return distance


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


choose_chickens = combinations(chicken, M)
distance = [{d: 0 for d in chicken} for _ in range(len(home))]
for i in range(len(home)):
    for ch in chicken:
        distance[i][ch] = abs(
            home[i][0]-ch[0])+abs(home[i][1]-ch[1])
answer = float('inf')
for choose_chicken in choose_chickens:
    tmp = 0
    for i in range(len(home)):
        mn = float('inf')
        for cc in choose_chicken:
            mn = min(mn, distance[i][cc])
        tmp += mn
    answer = min(tmp, answer)
print(answer)
