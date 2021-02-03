import sys, math
sys.stdin = open('tree_prob/baekjoon_11437.txt')

input = sys.stdin.readline

from collections import deque
# N<=50000, root는 1번에서 N번까지의 노드가 주어짐
# edge가 주어졌을 때(M<=10000) 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다. 

# 입력값에서 '\n' 지우기는 .split(' ')
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
    # 같은 노드면 무엇을 return 해야 하는가? 조상이니까 지금이 맞지 않나? 자기 자신인가봄
    # 처음부터 부모노드를 넣어주면 문제가 생김
    # 부모 노드의 부모 노드를 계속 넣어줬음...
    d,_ = p_arr[n1][0]
    d1 = d+1
    d,_ = p_arr[n2][0]
    d2 = d+1
    # 근데 이 경우 같으면 자기 자신 리턴인데?
    while d1 != d2:
        if d1 > d2: 
            d1, n1, d2, n2 = d2, n2, d1, n1
        diff = d2 - d1 
        l = int((math.log(diff,2)))
        d2, n2 = p_arr[n2][l]
    if n1 == n2:
        return n1
    else:
        while n1 != n2:
            d1, n1 = p_arr[n1][0]
            d2, n2 = p_arr[n2][0]
        return n1
        

N = int(input())
# 2N+1개 증가 여기에선 십만 1개 => 메모리 초과라서 바꿔줘야됨, 링크드로 전환
tree = [ [] for _ in range(N+1)]
# 간선 수는 N-1개
for _ in range(N-1):
    s,f = map(int, input().split(' '))
    tree[s].append(f)
    tree[f].append(s) 
#이 경우 N >=21이면?
k=int((math.log(N-1,2)))+1


p_arr,h= bfs(N,k)
# 트리는 노드 번호 순대로 있지 않다..., for문을 지양하자
print(p_arr)
print(h)
for i in h:
    d= p_arr[i][0][0]+1
    l = int(math.log(d,2))+1
    for l in range(1,l):
        p_arr[i][l] = p_arr[p_arr[i][l-1][1]][l-1]

# 메모리 초과가 나는지 안나는지 테스트 => 남
# 메모리 초과가 나므로 2^N개로 만듬, 희소행렬인데, 만약 이진트리의 경우 2^k개면 충분하기 때문에 이렇게 함
M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split(' '))
    print(lca(n1,n2))



# print(p_arr)
# 시간이 매우 오래 걸린다. 이걸 메모라이즈로 단축 가능한 줄 알았는데, input만 바꿔봐야겠다
# input이 많을때는 sys.stdin.readline을 써라 그래도 시간초과네

# 명심해라 트리는 노드번호 순대로 있지 않다.