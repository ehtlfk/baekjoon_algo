import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재,full인가 complete인가 conneted graph
# usado는 모든 usado 중 최솟값
# 단위가 매우 큼 최적화 필요
def dfs(s,node,mn):
    v[node] = 1
    for i in range(1,N+1):
        if v[i] == 0 and graph[node][i] != float('inf'):
            graph[s][i] = min(mn,graph[node][i])
            graph[i][s] = min(mn,graph[node][i])
            dfs(s,i,graph[node][i])
N, Q = map(int,input().split())
graph = [[float('inf')]*5001 for _ in range(5001)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p][q] = min(graph[p][q], r)
    graph[q][p] = min(graph[q][p], r)

for i in range(1,N+1):
    v= [0]*(N+1)
    dfs(i,i,float('inf'))
for _ in range(Q):
    K,V = map(int,input().split())
    cnt=0
    for i in range(1,N+1):
        if graph[V][i] >=K:# 자기 자신도 포함했구나..
            cnt+=1

    print(cnt-1)