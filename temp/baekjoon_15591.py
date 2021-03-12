import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재,full인가 complete인가 conneted graph
# usado는 모든 usado 중 최솟값
# 단위가 매우 큼 최적화 필요
def dfs(s,f):
    if graph[s][f] != float('inf'):
        return graph[s][f]
    for next in adj_list[s]:
        ret = min(graph[s][next],dfs(next,f))
    graph[s][f] = ret
    graph[f][s] = ret
    return ret
    
N, Q = map(int,input().split())
graph = [[float('inf')]*5001 for _ in range(5001)]
adj_list =[[] for _ in range(N+1)]
for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p][q] = min(graph[p][q], r)
    graph[q][p] = min(graph[q][p], r)
    adj_list[p].append(q)
    adj_list[q].append(p)

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if graph[i][j] == float('inf'):
            dfs(i,j)
    
for _ in range(Q):
    K,V = map(int,input().split())
    cnt=0
    for i in range(1,N+1):
        if graph[V][i] >=K:# 자기 자신도 포함했구나..
            cnt+=1

    print(cnt-1)


    # 아 node 5000개...