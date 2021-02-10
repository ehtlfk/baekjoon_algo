# 설탕을 배달하자
# 3과 5가 존재 최소 봉지의 개수
# 대표적인 동전문제
# 이걸 DP로 풀어봄
import sys

sys.stdin = open('DP_prob/baekjoon_2839.txt')
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    cnt = 0
    if N%5 == 0:
        cnt=(N//5)
    else:
        for i in range(N//5,0,-1):
            if (N-(i*5))%3 == 0:
                cnt+=i
                N-=i*5
                cnt+=N//3
                break
        else:
            if N%3==0:
                cnt = N//3
    if cnt:
        print(N,':',cnt)
    else:
        print(N,':',-1)