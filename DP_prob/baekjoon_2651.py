import sys

sys.stdin = open('DP_prob/baekjoon_2651.txt')
input = sys.stdin.readline

K = int(input())
s_num = int(input())

D = list(map(int, input().split(' ')))
d = 0
stops = list(map(int, input().split(' ')))

S = [0]*(s_num+1)
ans = set()

d = D[0]+D[1]
if D[0]+D[1] >K:
    S[1]=stops[0]
    ans.add(1)
    d = D[1]

    
for i in range(2,s_num+1):
    d += D[i]
    if d>K:
        s1 = S[i-1]+stops[i-1]
        s2 = S[i-2]+stops[i-2]
        # 정비소를 들리고 d를 안뺌
        # 아 같은 경우...
        S[i]= min(s1,s2)
        if s1 <= s2:
            ans.add(i)
            d = D[i]
        else:
            ans.add(i-1)
            d=D[i] + D[i-1]
            
    else:
        S[i] = S[i-1]
print(S[-1])
print(len(ans))
print(' '.join(map(str,ans)))
