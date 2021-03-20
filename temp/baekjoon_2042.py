import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# N<=10^6 M <=10^4 K<=10^4
# 부분합을 이용해야함, 백만이기 때문에 sum이 계속 반복됨
# 일정구간의 합은 (k1,k2)면, S2-S1하면됨
# 와 트리 문제라니 세상에
N,M,K = map(int,input().split())
seq = [int(input()) for _ in range(N)]

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        seq[b-1] = c
    elif a == 2:
        print(sum(seq[b-1:c]))

