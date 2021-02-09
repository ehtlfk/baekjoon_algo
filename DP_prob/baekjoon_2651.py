import sys

sys.stdin = open('DP_prob/baekjoon_2651.txt')
input = sys.stdin.readline

K = int(input())
s_num = int(input())

D = list(map(int, input().split(' ')))
stops = list(map(int, input().split(' ')))

S = [0]*(s_num+1)
ans = [[] for _ in range(s_num+1)]
d = D[0]

for i in range(1,s_num+1):
    d += D[i]
    if d>K:
        mn = K+1
        c = 0
        d = D[i]
        for j in range(i-1,-1,-1):
            if d >K:
                break
            temp = S[j]+stops[j]
            if mn > temp:
                c = j
                mn = temp
            d+=D[j]
        S[i] = mn
        ans[i].extend(ans[c])
        ans[i].append(c+1)
        d = sum(D[c+1:i+1]) 
    else:
        S[i] = S[i-1]
        ans[i].extend(ans[i-1])
print(S[-1])

print(len(ans[-1]))
if len(ans[-1]):
    print(' '.join(map(str,ans[-1])))

