import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

# 3~5 자리로 끊고 싶음
def d(s,l):
    if cache[s][l-3] != -1:
        return cache[c]
    if s+l >= len(pi):
        current =10
    else:
        for i in range(s,s+l):
            i+=1# 검사작업
    
   ret = 0
    for i in range(3):
        if l+i < 6:
            ret = min(ret,d(s+l,l+i))
    ret+=current
    # if len(pi)-c < 3:
    #     cache[c] = ret
    #     ret = 10

        
    cache[c] = ret        
    return ret


for _ in range(int(input())):
    pi = list(map(int,input()))
    cache = [[-1]*3 for _ in range(10003)]
    # cache = [-1]*10002 # +1,+2이므로
    d(0,3)