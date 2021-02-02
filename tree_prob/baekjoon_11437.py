import sys
sys.stdin = open('tree_prob/baekjoon_11437.txt')

from collections import deque
# N<=50000, root는 1번에서 N번까지의 노드가 주어짐
# edge가 주어졌을 때(M<=10000) 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다. 

# 입력값에서 '\n' 지우기는 .split(' ')
def bfs(n):
    queue = deque([1])
    v = [0]*(n+1)
    p = [0]*(n+1)
    p[1] = (0,0)
    d = 0
    
    while queue:
        l = len(queue)
        d+=1
        for _ in range(l):
            temp = queue.popleft()
            v[temp] = 1
            for i in tree[temp]:
                if v[i] == 0:
                    queue.append(i)
                    p[i] = (d,temp)
    return p

def lca(n1,n2):
    d1,p1 = p_arr[n1]
    d2,p2 = p_arr[n2]
    if p1 == p2:
        return p1
    
    while p1 != p2:
        if d1 > d2: 
            d1, p1,d2, p2 = d2, p2, d1, p1
        # 부모일경우
        if p2 == n1:
            return p2
        d2, p2 = p_arr[p2]
    
    return p1 

N = int(input())
# 2N+1개 증가 여기에선 십만 1개 => 메모리 초과라서 바꿔줘야됨, 링크드로 전환
tree = [ [] for _ in range(N+1)]
# 간선 수는 N-1개
for _ in range(N-1):
    s,f = map(int, input().split())
    tree[s].append(f)
    tree[f].append(s) 

p_arr = bfs(N)

M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())
    print(lca(n1,n2))




