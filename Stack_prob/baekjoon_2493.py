import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# N<=500,000 
# 낭낭하게 시간초과
N = int(input())

tower = list(map(int,input().split(' ')))

i = N-1
ans = [0]*(N)
while i >= 0:
    for j in range(i-1,-1,-1):
        if tower[i] <= tower[j]:
            for k in range(j+1,i+1):
                ans[k] = j+1
            i = j
            break
    else:
        i-=1
    
print(ans)