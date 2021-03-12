# 모든 조합을 다 뽑아봐야 하나?? 너무 많음
# 가장 긴 조합을 뽑아도, B 수열과 겹치면 정답이 되지 않음, 
# 가장 좋은 건 두개가 겹치지 않으면서 제일 긴거?
# n,m <=100
# 모든 원소들은 32비트 부호 있는 정수에 저장 가능, -1 있네
import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)



def jlis(idxA,idxB):
    if LIS[idxA+1][idxB+1] != -1:
        return LIS[idxA+1][idxB+1]
    ret = 2
    
    if idxA == -1:
        a = float('-inf')
    else:
        a = A[idxA]
    if idxB == -1:
        b = float('-inf')
    else:
        b = B[idxB] 
    mx = max(a,b)
    for i in range(idxA+1,N):
        if mx < A[i]:
            ret = max(ret, jlis(i,idxB)+1)
    for j in range(idxB+1,M):
        if mx < B[j]:
            ret = max(ret,jlis(idxA,j)+1)

    LIS[idxA+1][idxB+1] = ret
    return ret


for _ in range(int(input())):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    LIS = [[-1]*(M+1) for _ in range(N+1)]
    print(jlis(-1,-1)-2)
    
   
    print(LIS)
    # print(LIS2)
    # print(max(LIS2))
