import sys, math
sys.stdin = open('tree_prob/baekjoon_11725.txt')

input = sys.stdin.readline


def bfs(r):
    queue = [r]
    v = [0]*(N+1)
    while queue:
        temp = queue.pop(0)
        for node in tree[temp]:
            if v[node] == 0:
                v[node] = 1
                queue.append(node)
                parent[node] = temp 
     
N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s,f = map(int, input().split(' '))
    tree[s].append(f)
    tree[f].append(s)
parent = [0]*(N+1)
bfs(1)
for i in range(2,N+1):
    print(parent[i])
