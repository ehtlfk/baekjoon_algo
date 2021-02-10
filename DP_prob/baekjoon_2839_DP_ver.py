# 설탕을 배달하자
# 3과 5가 존재 최소 봉지의 개수
# 대표적인 동전문제, 그리디는 5의 배수인 숫자들을 계속 빼서 그 값이 3의 배수이면 값이 나오는 방식으로 하였는데, 과연 DP로는 어케 할까유?
# 이걸 DP로 풀어봄, **배열을 그리면 술술 풀린다** ,  배열을 그려서 한 칸 움직이면 5나 3이 바뀌는데, 3,5가 적은 값의 개수에서 둘중 작은 것을 골라 거기에 1을 더하면 된다.
import sys

sys.stdin = open('DP_prob/baekjoon_2839.txt')
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    s = [3000]*3001
    s[3] = 1
    s[5] = 1
    for i in range(6,N+1):
        s[i] = min(s[i-3], s[i-5])+1 
    if s[N]>=3000:
        print(N, ':', -1)
    else:
        print(N,':',s[N])