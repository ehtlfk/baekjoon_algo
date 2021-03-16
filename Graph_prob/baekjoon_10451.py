import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# 2<=N<=1000
def dfs(node):
    v[node] = 1
    if v[seq[node]] == 0:
        dfs(seq[node])
for _ in range(int(input())):
    N = int(input())
    seq = [0]
    seq.extend(list(map(int,input().split()))) # for 문 쓸거면 extend 써라
    v = [0]*(N+1)
    cnt = 0
    for i in range(1,N+1):
        if v[i] == 0:
            dfs(i)
            cnt+=1
    print(cnt)
