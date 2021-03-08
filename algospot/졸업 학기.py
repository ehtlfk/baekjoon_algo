import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
# 이 문제는 수가 많으면, BFS를 사용해서 풀어야 하지 않을까? 선수과목을 미리 수강해야 하므로

# 한 과목도 수강하지 않으면 휴학

for _ in range(int(input())):
    N, K, M, L = map(int, input().split())
    R = [0]*N
    C = [0]*M
    for i in range(N):
        r = list(map(int,input().split()))
        if r[0]:
            for j in range(r[0]):
                R[i] += ((1<<N)-1 & (1 << r[j+1]))
    
    for i in range(M):
        c = list(map(int,input().split()))
        if c[0]:
            for j in range(c[0]):
                C[i] += ((1<<N)-1 & (1 << c[j+1]))

    current = 0
    cnt = 0
    
    