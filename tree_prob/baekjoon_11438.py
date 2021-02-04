# 11437보다 4배는 빠르게 해야됨, 근데 희소행렬을 여기에서 쓰는 거 보면 1번을 잘 못 푼듯
# DFS가 더 빠른가???? 그럴지도?
# 해볼것 : DFS, memorize, 그 connect하는거?
# 다 필요없고, 높이가 같은데 부모가 다른 노드 개선, 부모가 같을 때까지 l값을 이동 없으면 가장 마지막 값 위 어딘가에 있음 => 개선완료


import sys, math
sys.stdin = open('tree_prob/baekjoon_11437.txt')

input = sys.stdin.readline

from collections import deque

def bfs(n,k):
    queue = deque([1])
    v = [0]*(n+1)
    p = [ [(0)]*k for _ in range(N+1) ]
    p[1][0] = (-1,1)
    d = 0
    h= []
    while queue:
        l = len(queue)
        d+=1
        for _ in range(l):
            temp = queue.popleft()
            v[temp] = 1
            for i in tree[temp]:
                if v[i] == 0:
                    queue.append(i)
                    p[i][0] = (d-1,temp)
                    # 더 좋은 게 있을거야
                    h.append(i)
    return p,h

def lca(n1,n2):
 
    d,_ = p_arr[n1][0]
    d1 = d+1
    d,_ = p_arr[n2][0]
    d2 = d+1
   
    while d1 != d2:
        if d1 > d2: 
            d1, n1, d2, n2 = d2, n2, d1, n1
        diff = d2 - d1 
        l = int((math.log(diff,2)))
        d2, n2 = p_arr[n2][l]
    if n1 == n2:
        return n1
    else:
        # 이부분을 개선해야하는데 이건 memorize?
        l=0
        while n1 != n2:
            if p_arr[n1][l]:
                d1, n1 = p_arr[n1][l]
                d2, n2 = p_arr[n2][l]
                l+=1
            else:
                d1, n1 = p_arr[n1][0]
                d2, n2 = p_arr[n2][0]
        return n1
        

N = int(input())

tree = [ [] for _ in range(N+1)]

for _ in range(N-1):
    s,f = map(int, input().split(' '))
    tree[s].append(f)
    tree[f].append(s) 
#이 경우 N >=21이면?
k=int((math.log(N-1,2)))+1


p_arr,h= bfs(N,k)

# print(p_arr)
# print(h)
for i in h:
    d= p_arr[i][0][0]+1
    l = int(math.log(d,2))+1
    for l in range(1,l):
        p_arr[i][l] = p_arr[p_arr[i][l-1][1]][l-1]

M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split(' '))
    print(lca(n1,n2))



