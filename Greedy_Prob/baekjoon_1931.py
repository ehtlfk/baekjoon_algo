import sys

sys.stdin = open('Greedy_Prob/baekjoon_1931.txt')
input = sys.stdin.readline

# 각 회의 시간이 겹치지 않게 되는 최대 회의의 개수

N = int(input())
T = [0]*N
for i in range(N):
    s,f = map(int, input().split(' '))
    diff = f-s
    T[i] = (s,f)

    # 이부분을 i로 하는 것은 조금 위험함, 문제는 없긴 한데... 이게 N^2라서 시간초과
    # 정렬: 버블, 퀵 sort, 
    # while i>0:
    #     diff2 = T[i-1][1] - T[i-1][0]
    #     if diff2 > diff:
    #         T[i-1], T[i] = T[i], T[i-1]
    #     elif diff2 == diff:
    #         if T[i-1][0] > T[i][0]:
    #             T[i-1], T[i] = T[i], T[i-1]
    #     else:
    #         break
    #     i-=1
# cnt =0
# s =0
# f =0
# for t in T:
#     s1,f1 = t
#     if f <= s1:
#         cnt+=1
#     s=s1
#     f=f1
# print(cnt)
# s_T = sorted(T, key=lambda x : (x[0],x[1]-x[0]))
s_T = sorted(T)
# 앞에 걸 기준으로 정렬 어떻게 하는 거임?
cnt = 0
s = 0
f = 0
for i in range(N):
    s1,f1 = s_T[i]
    if f<=s1:
        cnt+=1
        if s1 == f1:
            s = s1+1
            f = f1+1
        else:
            s = s1
            f = f1 
    elif s<=s1 and f1<=f:
        f = f1

    # 모두 같을 경우

        
print(cnt)