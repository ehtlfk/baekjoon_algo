# 계단의 개수가 300이하이므로 완탐문제가 아니었어??
# 2^300이 되나... 16개면 가능했는데 ㄲㅂ
# DP 문제인듯
import sys


sys.stdin = open('baekjoon_2579.txt')

input = sys.stdin.readline

def step(d, total):
    global mx
    if d == stairs_num:
        if total > mx:
            mx = total
    else:
        if v[d-1] == 0:
            v[d+1] = 1
            step(d+1,total+point_list[d])
            v[d+1] = 0
        if d+2 < stairs_num+1:
            v[d+2]=1
            step(d+2,total+point_list[d])
            v[d+2]=0


stairs_num=int(input())
point_list=[0]*(stairs_num+1)
for i in range(stairs_num):
    point_list[i+1] = int(input())
mx = point_list[-1]
v = [0]*(stairs_num+1)
step(0,mx)
print(mx)