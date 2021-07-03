# 2마리 이상의 상어일 경우 가장 큰 상어가 다잡아먹음 -> 크기가 같은 경우는? 상어의 방향을 정해야함
import sys,os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

R,C,M = map(int,input().split())

arr = [ list(map(int,input().split())) for _ in range(M)]
answer = 0

mat = [[-1]*C for _ in range(R)]

for i in range(M):
    mat[arr[i][0]-1][arr[i][1]-1] = i

for p in range(C):
    for r in range(R):
        shark = mat[r][p]
        if shark != -1:
            answer+=arr[shark][4]
            mat[r][p] = -1
            arr[shark] = None
            break
    
    for j in range(M):
        if arr[j]!=None:
            if mat[arr[j][0]-1][arr[j][1]-1] == j:
                mat[arr[j][0]-1][arr[j][1]-1] = -1 # 이게 이거 이전의 샤크가 사라질 수 있음
            
            s = arr[j][2]
            d = arr[j][3]
            while s>0:
                if d == 1:
                    arr[j][0]-=(s%(2*R-2))
                    if arr[j][0] <= 0:
                        d =2
                        s = arr[j][0]*-1+1
                        arr[j][0] = 1
                    else:
                        break
                elif d == 2:
                    arr[j][0]+=(s%(2*R-2))
                    if arr[j][0] > R:
                        d = 1
                        s = arr[j][0]-R
                        arr[j][0] = R
                    else:
                        break
                elif d == 3:
                    arr[j][1]+=(s%(2*C-2))
                    if arr[j][1]>C:
                        d = 4
                        s = arr[j][1]-C
                        arr[j][1] = C
                    else:
                        break
                elif d == 4:
                    arr[j][1]-=(s%(2*C-2))
                    if arr[j][1] <= 0:
                        d = 3
                        s = arr[j][1]*-1+1
                        arr[j][1] = 1
                    else:
                        break
            arr[j][3] = d
            mx = mat[arr[j][0]-1][arr[j][1]-1]
            if mx == -1:
                mat[arr[j][0]-1][arr[j][1]-1] = j
            elif mx < j:
                if arr[mx][4] < arr[j][4]:
                    arr[mx] = None
                    mat[arr[j][0]-1][arr[j][1]-1] = j
                else:
                    arr[j] = None
            else:
                mat[arr[j][0]-1][arr[j][1]-1] = j
print(answer)