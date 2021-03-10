import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)


# N<=100 ... C로 풀자
def recursion(x,y):
    if x>=N or y>=N:
        return False
    if x == N-1 and y == N-1:
        return True
    if cache[x][y] != -1:
        return cache[x][y]
    cache[x][y] = (recursion(x+mat[x][y],y) or recursion(x,y+mat[x][y]))
    return cache[x][y]
for _ in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    # 0으로 초기화를 하면 안됨, x,y 점을 방문했는지 안했는지를 알 수 없음
    cache = [[-1]*N for _ in range(N)]
    if recursion(0,0):
        print('YES')
    else:
        print('NO')
