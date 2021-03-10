import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline
# extend는 None을 리턴해서 0으로 했는데, 먼가 아쉽



for _ in range(int(input())):
    N = int(input())
    # tree = [[0]*N for _ in range(N)]
    # for i in range(N):
    #     tree[i] = list(map(int,input().split()))
    #     tree[i].extend([0]*(N-i-1))
    tree = [list(map(int,input().split()))+ [0]*(N-i-1) for i in range(N) ] 
    for i in range(1,N):
        for j in range(i+1):
            tree[i][j] += max(tree[i-1][j],tree[i-1][j-1]) 
    print(max(tree[-1]))