import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# 돈뽑 시간이 짧은 친구를 앞으로 보냅시다.

N = int(input())

p = sorted(map(int,input().split()))
total = 0
temp = 0
for i in range(N):
    temp +=p[i]
    total+=temp
print(total)
