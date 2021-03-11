import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

# 3~5 자리로 끊고 싶음
def check(s,l):
    if s+l>len(pi):
        return 10
    temp = pi[s+1]-pi[s]
    for i in range(s+1,s+l):
        if pi[s] == pi[i]:
            continue
        if pi[i]-pi[i-1] == temp:
            temp=pi[i]-pi[i-1]
            continue
        if i%2 == 0: 
            if pi[0] == pi[i]:
                temp = float('inf')
                continue
        if i%2 ==1:
            if pi[1] == pi[i]:
                temp = float('inf')
                continue
        return 10
    if temp == float('inf'):
        return 4
    if abs(temp) == 1:
        return 2
    if abs(temp) == 0:
        return 1
    return 5
def d(s,l):
    if cache[s][l-3] != -1:
        return cache[s][l-3]

    if s+l > len(pi):
        cache[s][l-3] = 10
        return 10
    else:
        current = check(s,l)
    
    if s+l == len(pi):
        return current
    ret = float('inf')
    for i in range(3):
        ret = min(ret,d(s+l,i+3))
    
    ret+=current

    cache[s][l-3] = ret        
    return ret


for _ in range(int(input())):
    pi = list(map(int,input()))
    cache = [[-1]*3 for _ in range(10003)]
    # cache = [-1]*10002 # +1,+2이므로
    mn = float('inf')
    for i in range(3,6):
        mn = min(mn,d(0,i))
    print(mn)
 

    # print(check(5,3))