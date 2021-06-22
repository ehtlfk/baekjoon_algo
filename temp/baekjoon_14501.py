import sys
import os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] + '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


def recursion(n, k, total):
    global mx
    # if n == k:
    #     total += table[k-1][1]
    if n <= k:
        if total > mx:
            mx = total
        return
    else:
        recursion(n, k+1, total)  # 일 안함
        if k+table[k][0] < n+1:
            recursion(n, k+table[k][0], total+table[k][1])  # 일 함


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

mx = 0
recursion(N, 0, 0)
print(mx)
