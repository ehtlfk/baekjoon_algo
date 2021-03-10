import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)

for _ in range(int(input())):
    N = int(input())
    seq = list(map(int,input().split()))
    LIS = [1]*N
    for i in range(1,N):
        if seq[i-1]< seq[i]:
            LIS[i] = LIS[i-1]+1
    print(max(LIS))
    