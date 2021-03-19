import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


# 바이토닉 수열
# Sk는 항상 최대값, 그 값을 기준으로 바이토닉이면 바이토닉 수열
# 최대값이 여러개
# 이어져 있지 않은 부분 수열
# 최대값을 기준으로, 최대값이 Sk오른쪽이면 Sk는 최대값이어야 최대 길이,  왼쪽일 경우 역시, Sk 가 최대값이어야 최대 길이
# 그러면 최대값을 구하고, 최대값을 제외한 상태에서 바이토닉 최장 길이를 구함 => 재귀인가?
# 각 order에 해당하는 index값을 저장해야하나?


def bio(k,n): # n: 최대값 idx
    if k == n:
        return
    mx = 0
    for i in range(k+1,n):
        if seq[i] == seq[n]:
            continue
        elif seq[k] < seq[i]:
            mx = max(mx,bio(i,n)+1)
    return mx

N = int(input())

seq = list(map(int,input().split()))
order = sorted(list(set(seq)))


# print(bio(len(order)-1))
mx = 0
mx_list= []
for i in range(N):
    if seq[i] > mx:
        mx = seq[i]
        mx_list = []
        mx_list.append(i)
    elif seq[i] == mx:
        mx_list.append(i)

answer = 0
for i in mx_list:
    check = [0]*N
    check[0] = 1
    temp = 0
    for j in range(N):
        if seq[j] == seq[i] and i!=j:
            continue
        if i>j:# 증가
            if seq[j] > seq[temp]:
                check[j]= check[temp]+1
                temp = j
            else:
                check[j] = check[temp]
                temp = j
        elif i<j:# 감소
            if seq[j] < seq[temp]:
                check[j] = check[temp]+1
                temp = j
            else:
                check[j] = check[temp]
                temp = j 
        else:
            check[j] = check[temp]+1
            temp = j
        answer = max(answer,max(check))
    print(check)
print(answer)