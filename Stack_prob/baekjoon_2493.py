import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# N<=500,000 
# 낭낭하게 시간초과
# 설마 높이가 같으면 수신 못하나? 와 N개의 서로 높이가 다른 탑이넹...
N = int(input())

tower = list(map(int,input().split(' ')))
index = list(range(N))
stack = []
ans = [0]*N
temp = index.pop()
while index:
    if tower[temp] < tower[temp-1]:
        ans[temp] = temp
        while stack:
            if tower[stack[-1]] < tower[temp-1]:
                ans[stack.pop()] = temp 
            else:
                break
    else:
        stack.append(temp)
    temp = index.pop()

    
print(' '.join(map(str,ans)))