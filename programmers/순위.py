# 단방향 그래프를 그려라
# 갈라지는 점을 찾으면 되는데... 이런 건 보통 bfs인데
# 일단 root를 찾음 어케하냐면, 값을 받아올때 하면됨
# 컴포넌트가 2 이상이면 0개임, 즉 root가 2개 이상이어도 컴포넌트는 1개일 수 있구나 
# 아 최대 depth를 알면되네
# dfs 였다.

# 중복된 숫자 제외한 개수
d = [0,4,4,3,2,1,1,0,0]
# cnt = 0
# l = len(sd)
# stack =[sd.pop()]
# while sd:
#     temp =sd.pop()
#     if temp == stack[-1]:
#         cnt+=1
#     else:
#         if cnt:
#             l-=cnt+1 
#         cnt = 0
#         stack.append(temp)
# if cnt:
#     l-=cnt+1
# answer = l
# print(answer)

# check = [1]*(len(d))
# for i in range(1,len(d)):
#     for j in range(i+1, len(d)):
#         if d[i] == d[j]:
#             check[d[i]] = 0
# answer = sum(check)-1
# print(answer)
# print(check)



def dfs(r,g,d,p):
    for e in g[r]:
        if d[e] == 0:
            d[e] = d[r]+1
            p[e] = r
            dfs(e,g,d,p)
        elif d[e] != d[r]-1:
            d[e] = d[r]+1
            
def solution(n, results):
    
    g = [[] for _ in range(n+1)]
    r = [0]*(n+1)
    roots =[]
    for res in results:
        s,f = res
        g[f].append(s)
        r[s] = 1
    for i in range(1,n+1):
        if r[i] == 0:
            roots.append(i)
    cnt = []
    d = [0]*(n+1)
    p = [0]*(n+1)
    
    for root in roots:
        dfs(root,g,d,p)
        
    check = [1]*(max(d)+1)
    for i in range(1,len(d)):
        for j in range(i+1, len(d)):
            if d[i] == d[j]:
                check[d[i]] = 0
    answer = sum(check)
    
    
    leaf = []
    for i in range(1,n+1):
        if not g[i]:
            leaf.append(i)
    
    if len(leaf) > 1 and check[max(d)] == 1:
        answer-=1
    
    print(d)  
        
    return answer


def bfs(r,g,n):
    queue = [r]
    v= [0]*(n+1)
    while queue:
        temp = queue.pop(0)
        for e in g[temp]:
            if v[e] == 0:
                v[e] = 1
                queue.append(e)
    return sum(v)
        
            
def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    win_cnt = [0]*(n+1)
    lose_cnt = [0]*(n+1)
    
    for res in results:
        s,f = res
        win[f].append(s)
        lose[s].append(f)
    for i in range(1,n+1):
        win_cnt[i] = bfs(i,win,n)
    for i in range(1,n+1):
        lose_cnt[i] = bfs(i,lose,n)
        
    for x,y in zip(win_cnt,lose_cnt):
        if x+y == n-1:
            answer+=1
        
    return answer


    # 이 문제의 핵심은 한 정점이 이긴 정점과 진 정점의 개수 합이 N-1일 경우 순위가 결정이 되는 것이다. 이것을 위해 단방향 그래프 두 개를 이용하여 한 쪽은 이기는 정점, 반대쪽은 지는 정점의 개수를 조사하도록 코드를 작성. 
    # 모든 정점에 대해 자신이 이기는 정점과 지는 정점을 bfs나 dfs를 이용하여 개수를 셈. 단방향 그래프이기 때문에 다른 방향으로는 가지 않는다.

    # 모든 정점에 대해 탐색을 하므로 속도가 느리다. 부모와 조상 관계로 이것을 줄일 수도 있을 것 같다.