# 11437보다 4배는 빠르게 해야됨, 근데 희소행렬을 여기에서 쓰는 거 보면 1번을 잘 못 푼듯
# DFS가 더 빠른가???? 그럴지도?
# 해볼것 : DFS, memorize, 그 connect하는거?
# 다 필요없고, 높이가 같은데 부모가 다른 노드 개선, 부모가 같을 때까지 l값을 이동 없으면 가장 마지막 값 위 어딘가에 있음 => 개선완료

# unpacking 할때 시간이 드나?
import sys, math, time
# sys.stdin = open('tree_prob/baekjoon_11437.txt')
sys.stdin = open('test.txt')

input = sys.stdin.readline

from collections import deque

def bfs(n,k):
    queue = deque([1])
    v = [0]*(n+1)
    p = [ [0]*k for _ in range(n+1) ]
    p[1][0] = 1
    d = 0
    h= []
    depth= [0]*(n+1)
    depth[1] = 0
    while queue:
        l = len(queue)
        d+=1
        for _ in range(l):
            temp = queue.popleft()
            v[temp] = 1
            for i in tree[temp]:
                if v[i] == 0:
                    queue.append(i)
                    p[i][0] = temp
                    depth[i] = d
                    h.append(i)     
    return p,h, depth

def lca(n1,n2):
 
    d1 = depth[n1]
    d2 = depth[n2]
   
    while d1 != d2:
        if d1 > d2: 
            d1, n1, d2, n2 = d2, n2, d1, n1
        diff = d2 - d1 
        l = int((math.log(diff,2)))
        n2 = p_arr[n2][l]
        d2 = depth[n2]
    if n1 == n2:
        return n1
    else:
        # 이부분을 개선해야하는데 이건 memorize?
        # 생각해보니 같은 경우가 나와도 그게 최소란 보장이 l이 끝까지 가야 생김
        # d1을 이용해서 l값을 구할 수 있어
        # temp로 받아야 한 배열의 값을 다 순환할 수 있음, 값을 변경해서는 안됨
        l = int((math.log(d1,2)))+1
        for i in range(1,l):
            temp1 = p_arr[n1][i]
            temp2 = p_arr[n2][i]
            if temp1 == temp2:
                n1 = p_arr[n1][i-1]
                n2 = p_arr[n2][i-1]
                d1 = depth[n1]
                d2 = depth[n2]
                break
        while n1 != n2: 
            n1 = p_arr[n1][0]
            n2 = p_arr[n2][0]
        return n1
        
start = time.time()
N = int(input())

tree = [ [] for _ in range(N+1)]
for _ in range(N-1):
    s,f = map(int, input().split(' '))
    tree[s].append(f)
    tree[f].append(s) 
#이 경우 N >=21이면?
k=int((math.log(N-1,2)))+1



p_arr,h,depth = bfs(N,k)
# 사실 이 친구가 젤 오래 걸리는데?
# 트리에 따라 다른데 편향일 경우, bfs는 얼마 안걸림
# h는 100,000, l 은 max 16 => 160만
for i in h:
    # 현재 노드의 높이
    d= depth[i] 
    l = int(math.log(d,2))+1
    for l in range(1,l):
        p_arr[i][l] = p_arr[p_arr[i][l-1]][l-1]

M = int(input())
ans = [0]*M
for m in range(M):
    n1, n2 = map(int, input().split(' '))
    ans[m] = lca(n1,n2)
# print('\n'.join(map(str,ans)))

print("time :", time.time() - start)

