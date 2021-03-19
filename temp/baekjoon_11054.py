import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 바이토닉 수열
# Sk는 항상 최대값, 그 값을 기준으로 바이토닉이면 바이토닉 수열
# 최대값이 여러개
# 이어져 있지 않은 부분 수열
# 최대값을 기준으로, 최대값이 Sk오른쪽이면 Sk는 최대값이어야 최대 길이,  왼쪽일 경우 역시, Sk 가 최대값이어야 최대 길이

# 반례 9 1 2 3 4 5 6

# 그러면 최대값을 구하고, 최대값을 제외한 상태에서 바이토닉 최장 길이를 구함 => 재귀인가?
# 각 order에 해당하는 index값을 저장해야하나?

# 현재 위치에서 자신보다 큰 값의 개수를 구함, 메모이제이션을 해야하나?

def bio(k,n): # n: 최대값 idx
    if cache[k][n]!=-1:
        return cache[k][n]
    mx = 0

    for i in range(k+1,n+1):
        if seq[k] < seq[i]:
            mx = max(mx,bio(i,n)+1)

    if cache[k][n] == -1:
        cache[k][n] = mx
    return mx

def bio2(k,n):
    if cache[k][n]!=-1:
        return cache[k][n]
    mx = 0
    for i in range(k-1,n-1,-1):
        if seq[k] < seq[i]:
            mx = max(mx,bio2(i,n)+1)
    if cache[k][n] == -1:
        cache[k][n] = mx
    return mx

N = int(input())
seq = list(map(int,input().split())) # mx

ans = 0
cache = [[-1]*N for _ in range(N)]
for x in range(N):
    
    m1 = 0
    m2 = 0  
    for i in range(x):
        m1 = max(m1,bio(i,x))
    for k in range(N-1,x,-1):
        m2 = max(m2,bio2(k,x))
    
    ans = max(ans,m1+m2)

print(ans+1)