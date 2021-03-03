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

check = [1]*(len(d))
for i in range(1,len(d)):
    for j in range(i+1, len(d)):
        if d[i] == d[j]:
            check[d[i]] = 0
answer = sum(check)-1
print(answer)
print(check)