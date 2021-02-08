# 계단의 개수가 300이하이므로 완탐문제가 아니었어??
# 2^300이 되나... 16개면 가능했는데 ㄲㅂ
# DP 문제인듯
# 너무 오래걸렸다 푸는데, 이 간단한걸 너무 어렵게 생각했다
import sys


sys.stdin = open('baekjoon_2579.txt')

input = sys.stdin.readline


stairs_num=int(input())
p=[0]*(stairs_num)
for i in range(stairs_num):
    p[i] = int(input())
points =[0]*(stairs_num)
check = [0]*(stairs_num)
# N이 2이상이어야 성립함
for i in range(stairs_num):
    if i > 1:
        points[i] = max(p[i]+p[i-1]+points[i-3], p[i]+points[i-2])
    else:
        points[i]= p[i]+points[i-1]
print(points[-1])