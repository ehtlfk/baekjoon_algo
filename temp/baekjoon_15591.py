import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 **하나** 존재,full인가 complete인가 conneted graph
# usado는 모든 usado 중 최솟값
# 단위가 매우 큼 최적화 필요
# 한 노드에서 다르 노드로 가는 경로가 단 하나! 
# -> 트리, 각 노드의 조상을 구하고 최소값을 구해놓은 뒤, lca를 구하면 리프 노드에서 리프 노드까지의 유사도를 알 수 있다.
def dfs(s,f):
    v[s] = 1
    # if graph[s][f] != float('inf'):
    #     return graph[s][f]
    for n in adj_list[s]:
        if v[n] == 0:
            ret = min(graph[prev][s], dfs(n, f))
            graph[prev][n] = ret
            graph[n][prev] = ret
    node.append(s)
    # return graph[prev][s]
    # for next in adj_list[s]:
    #     ret = min(graph[s][next],dfs(next,f))
    # graph[s][f] = ret
    # graph[f][s] = ret


def bfs(s, f):
    v[s] = 1
    for i in adj_list[s]:
        v[i] = 1
    queue = adj_list[s]

    while queue: # s==f일경우
        temp = queue.pop(0)
        if temp == f:
            break
        for next in adj_list[temp]:
            if graph[s][next] == float('inf') and v[next] == 0:
                v[next] = 1
                ret = min(graph[temp][next],graph[s][temp])
                graph[s][next] = ret
                graph[next][s] = ret
                queue.append(next)
                

N, Q = map(int,input().split())
graph = [[float('inf')]*5001 for _ in range(5001)]
adj_list =[[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p][q] = min(graph[p][q], r)
    graph[q][p] = min(graph[q][p], r)
    adj_list[p].append(q)
    adj_list[q].append(p)

# for i in range(1,N+1):
    # for next in adj_list[i]:

for i in range(1,N+1):
    v = [0]*(N+1)
    bfs(i)
for i in range(1,5):
    print(graph[i][1:5])

for _ in range(Q):
    K,V = map(int,input().split())
    cnt=0
    for i in range(1,N+1):
        if V!=i and graph[V][i]>=K:
            cnt+=1
    # for i in range(1,N+1):
    #     if graph[V][i] >=K:# 자기 자신도 포함했구나..
    #         cnt+=1

    print(cnt)


    # 아 node 5000개...