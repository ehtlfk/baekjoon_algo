import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# 일단 정렬
# 가장 단순한 생각: 최솟값 * N, 하지만, 최소값을 버리고 들을 수 있다.( 1,10,20 )
# 최대값*k,  최대값 vs k*최소값 해서 더 큰 쪽이 답

N = int(input())

rope = [int(input()) for _ in range(N)]

srope = sorted(rope,reverse=True)
mx = srope[0]
for i in range(1,N):
    if mx < srope[i]*(i+1):
        mx = srope[i]*(i+1)
print(mx)