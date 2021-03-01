def check(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            cnt+=1
    if cnt == len(w1)-1:
        return True
    else:
        return False
def dfs(begin, target,words,v):
    global answer, mn
    # 너비 우선 탐색, nope dfs
    v[begin] = 1
    if begin== target:
        if answer < mn:
            mn = answer
        return
    elif len(v) == len(words):
        return
    else:
        for w in words:
            if not v.get(w,0) and check(begin,w):
                answer+=1
                dfs(w,target,words,v)

answer = 0
mn = 0
def solution(begin, target, words):
    v={begin: 1}
    dfs(begin,target,words,v) 
    print(answer)
    return answer


# 이 풀이 말고 bfs일때는 일치하지 않는 단어들을 이용해서 for 문을 돌려서 구할 수도 있음
# total 값을 넘기는 방법은 prev index 인자의 값을 계속 더해나가는것