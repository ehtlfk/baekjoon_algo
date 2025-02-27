

def bfs(c, b):
    t = 0
    queue = [(b,t)]
    mx = 200000
    v = [(0,0)]*(mx+1)
    vc = [0]*(mx+1) # t일때의 c의 위치를 알기 위해서, 안쓰려면 while ~ for queue.size() t++ 식으로 작성해야됨
    vc[t] = c
    while queue:
        
        b,t = queue.pop(0)
        c = vc[t]
        if not vc[t+1]:
            vc[t+1] = c + t+1
        if b > 200000:
            return -1
        if vc[t] == b:
            return t

        if 0<= 2*b <= mx:
            if v[2*b][0] == 0 or v[2*b][1] !=t+1: # (나중에 도달한 시간, 현재 시간+1) 이걸로 (32,5), (32,6) 해결
                queue.append((2*b,t+1))
                v[2*b] = (v[b][0]+1,t+1)

        if 0 <= b-1 <= mx:
            if v[b-1] == 0 or v[b-1][1] !=t+1:
                queue.append((b-1, t+1))
                v[b-1] = (v[b][0]+1,t+1)

        if 0<= b+1 <= mx:
            if v[b+1] == 0 or v[b+1][1] !=t+1:
                queue.append((b+1,t+1))
                v[b+1] = (v[b][0]+1,t+1)

def bfs2(c,b):
    v = [[0]*2 for _ in range(200001)] # tuple로 선언하면 변경 불가, 이런 식으로 선언해야 의도한 대로 된다. [[0,0]]*N은 다바뀜
    t = 0
    queue = [b]
    mx = 200001
    while True:
        l = len(queue)
        c += t
        if c > 200001:
            return -1
        if v[c][t%2]:
            return t
        
        for _ in range(l):
            b = queue.pop(0)

            current_time = (t+1)%2 # t+1을 해줘야 다음 시간임
            if 0<= 2*b < mx:
                if v[2*b][current_time] == 0:
                    queue.append(2*b)
                    v[2*b][current_time]  = t+1

            if 0 <= b-1 < mx:
                if v[b-1][current_time] == 0:
                    queue.append(b-1)
                    v[b-1][current_time] = t+1

            if 0<= b+1 < mx:
                if v[b+1][current_time] == 0:
                    queue.append(b+1)
                    v[b+1][current_time] = t+1
        t+=1

print(bfs(11,1))
print(bfs(11,2))
print(bfs(6,3))
print(bfs2(11,1))
print(bfs2(11,2))
print(bfs2(6,3))
# t = 0
# location =[(11,1)]
# while True:
#     if t>200000:
#         return -1
    
#     if t%2:

#     else:

#     t+=1

# 32 위치에 5초에 도작함, 하지만 위 코드는 6초에 도작하는 걸 고려하지 않음 
# 32일때 만나지만, 39 일 때 만나는걸 더 먼저함 queue이기 때문
# 어렵네
# t에서 둘의 위치
# 11,1 (32,6)이 안들어감 (32,5)를 넣으면서 했으므로
# 6,3  12를 2초 만에 가지만, 3초에 12에 갈 수 없음

# 하지만 짝수와 홀수를 구분하는 게 더 효율 적인 알고리즘 !
# t에 대해서 t == t+2 but t != (t+1 or t-1) 
# C의 t초 후 위치
# B의 t초 후 위치가 1 2 4 8 이면, t-2k는 이거와 같음
# 짝수 홀수로 고려해야하는 이유 같은 위치가 짝수 시간 홀수 시간 2개 밖에 존재할 수 없다. 32 6초 32 5초  ,32 6초 8초는 다가능 여기서부터 갱신하면 됨
# 즉 32초에 최초로 도달할수 있는 시간은 5초와 6초임, 5초에 처음 방문하고 7초는 방문함, 6초도 방문한다면, 5,7,9 6,8,10 으로 갱신이 됨
# 4초에는 도달 불가능, 3초도 불가능이므로 답은 6초가 됨