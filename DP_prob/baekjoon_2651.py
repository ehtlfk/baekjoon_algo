import sys

sys.stdin = open('DP_prob/baekjoon_2651.txt')
input = sys.stdin.readline

K = int(input())
s_num = int(input())

D = list(map(int, input().split(' ')))
d_stack = [0]*(s_num+1)
d_stack[0] = D[0]
for i in range(1,s_num+1):
    d_stack[i]=D[i]+d_stack[i-1]
stops = list(map(int, input().split(' ')))

S = [0]*(s_num+1)
ans = set()
if d_stack[1] >K:
    S[1]=stops[0]
    ans.add(1)

for i in range(2,s_num+1):
    l = d_stack[i]//K
    mn = 10000000
    c = 0
    for j in range(l):
        if D[i-l]+D[i+l-1] <= K:
            temp = S[i-l]+stops[i-l]
            if mn > temp:
                mn = temp
                c = i-l+1
            # s2 = S[i-2]+stops[i-2]
            # S[i]= min(s1,s2)
            # if s1> s2:
            #     ans.add(i-1)
            # else:
            #     ans.add(i)
        else:
            S[i] = S[i-l]+stops[i-l]
            ans.add(i-l+1)
    if l:
        ans.add(c)
        S[i] = mn
print(S)
print(len(ans))
print(' '.join(map(str,ans)))
print(stops, d_stack, D)