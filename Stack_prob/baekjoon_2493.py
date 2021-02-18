import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# N<=500,000 
# 낭낭하게 시간초과
N = int(input())

tower = list(map(int,input().split(' ')))


ans = [0]*(N)

for i in range(1,N):
    if tower[i-1] >= tower[i]:
        ans[i] = i
    else:
        if ans[i-1]:
            if tower[ans[i-1]-1] >= tower[i]:
                ans[i] = ans[i-1]
    
print(ans)