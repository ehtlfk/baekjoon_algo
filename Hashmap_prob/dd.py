import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


N = int(input())

dd = [ list(map(int,input().split())) for _ in range(N**2) ]
        


# 생각해보니 해쉬맵이 있다. 이거 500개밖에 안되잖아