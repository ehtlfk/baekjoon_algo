# bfs


def bfs(node,n,g):
    queue = [node]
    v = [0]*(n+1)
    v[1] = 1
    while queue:
        temp = queue.pop(0)
        for child in g[temp]:
            if v[child] == 0:
                v[child] = v[temp]+1
                queue.append(child)
    return v

def solution(n, edge):
    answer = 0
    
    g = [ []  for _ in range(n+1) ] 
    for node in edge:
        s,f = node
        g[s].append(f)
        g[f].append(s)
    
    v = bfs(1,n,g)    
    mx = max(v)
    for i in v:
        if i == mx:
            answer+=1
    return answer

    # v 를 다시 찾는 부분이 마음에 들지 않음
    # bfs 함수의 for문에서 cnt를 하는 방법이 더 빠름