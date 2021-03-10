import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)


# i를 끝으로 하는 LIS 값이 LIS[i] 
for _ in range(int(input())):
    N = int(input())
    seq = list(map(int,input().split()))
    LIS = [1]*N
    for i in range(1,N):
        mx = 0
        for j in range(i-1,-1,-1):
            if seq[j] < seq[i]:
                if mx < LIS[j]:
                    mx = LIS[j]
        LIS[i] = mx+1

 
    print(max(LIS))
    print(LIS)