import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input())

K = int(input())

sensor = sorted(map(int,input().split(' ')))
# 최솟값 찾는게 더빠르네?
sub = [0]*(N-1)
for i in range(N-1):
    sub[i] = sensor[i+1] - sensor[i] 
    
s_sub = sorted(sub)
# N<K이면 안되는구나
for _ in range(K-1):
    if s_sub:
        s_sub.pop()
    else:
        break
print(sum(s_sub))