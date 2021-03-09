# 이 문제의 핵심은 나눴을 때 좌우를 합쳐야 최대 넓이가 나온다면, 항상 좌우 양쪽의 두 판자가 포함된다는 것이다. 그러므로 중앙에서 확장시켜
# 나가면서 문제를 해결할 수 있다.

import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

def extend_fence(left, right,cnt):
    if left <0:
        return
    l= 0 
    r = 0
    if 0 <= left:
        l = fence[left]
    if right < N:
        r = fence[right]
    if l>r:
        c = l
        left-=1
    else:
        c = r
        right+=1
    mx[cnt] = min(c,mx[cnt-1]//cnt)*(cnt+1)
    extend_fence(left,right,cnt+1)


for _ in range(int(input())):
    N = int(input())
    fence = list(map(int,input().split()))

    mx = [0]*N
    l = len(fence)//2
    mx[0] = fence[l]
   
    extend_fence(l-1,l+1,1)
    mx.extend(fence)
    print(max(mx))