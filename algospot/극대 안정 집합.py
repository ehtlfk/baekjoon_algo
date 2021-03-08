N = 4
explode = [2,1,8,4] # explode[i]와 i가 합쳐지면 터짐
ret = 0
ans =[]
def isStable(num):
    for i in range(N):
        # 이 문제에선, num & 1<<i는 i번째 원소가 있다는 것을 가리킴, 이 i 번째 원소가 있는 넘이랑 같이 두고 num이랑 교집합을 해서
        # 같은게 있으면 터짐, 아 반대로 되어있구나... A가 i=3일때구나, 순서를 잘 정하자, i<<N이기 때문에 0001, 0010, 0100,1000 순으로 감
        if (num & 1<<i) and (num & explode[i]):
            return False
    return True
for i in range(1, 1<<N): # i는 1~ 15, 모든 부분 집합
    if not isStable(i): # 여기 걸리는건 explode와 합집합을 했을 때 터지는 i 
        continue
    canExtend = False
    for add in range(N):
        if i & (1<<add) == 0 and (explode[add] & i) == 0:
            canExtend = True
            break
    if not canExtend:
        ret+=1
        ans.append(i)
print(ans)
print(ret)