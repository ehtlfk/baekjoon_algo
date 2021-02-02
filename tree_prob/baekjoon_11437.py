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
    p[1] = (0,1)
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
    # 같은 노드면 무엇을 return 해야 하는가? 조상이니까 지금이 맞지 않나? 자기 자신인가봄
    # 처음부터 부모노드를 넣어주면 문제가 생김
    d,_ = p_arr[n1]
    d1,p1 = d+1,n1
    d,_ = p_arr[n2]
    d2,p2 = d+1,n2
    # 근데 이 경우 같으면 자기 자신 리턴인데?
    while p1 != p2:
        # 높이가 같을 경우 부모가 한쪽으로 감
        if d1 > d2: 
            d1, p1, d2, p2 = d2, p2, d1, p1
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



# 시간이 매우 오래 걸린다. 이걸 메모라이즈로 단축 가능한 줄 알았는데, input만 바꿔봐야겠다