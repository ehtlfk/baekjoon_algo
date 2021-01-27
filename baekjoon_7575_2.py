import sys
sys.stdin = open('input.txt')

# 접근방식을 문자열을 K개 만큼으로 쪼개서 KMP 탐색을 하는 것으로 바꿈, K개 이상이라는 말은 함정같음
# 이제 시간초과는 되지 않음
N, K = map(int, input().split())
mat = [0]*N
for i in range(N):
    mi = input()
    mat[i] = list(map(int,input().split()))

# n<=100, M<=1000
def pi(arr): # 전부 검사에도 쓸 수 있음
    l = len(arr)
    i = 0
    if l%2:
        j = l//2+1
    else:
        j = l//2 # 실수되었던가?
    p = 0
    while i < l//2:
        if arr[i] == arr[j]:
            p+=1
        i+=1
        j+=1
    return p

def check(A,B):
    a=A;b=B
    if len(A) < len(B):
        a,b = B,A

    # b를 토막냄
    common = []
    for j in range(len(b)-(K-1)):
        i = 0
        while i < len(a) - (K-1):
            c = 0
            for k in range(K): 
                if a[i+k] == b[j+k]:
                    c+=1
                else:
                    temp = pi(b[j:j+c])
                    if c and temp : # c값이 없으면 i+=1
                        i+= K - temp # 1을 더하면 안됨, 그리고 pi가 0이면 ? ################
                    else:
                        i+=1
                        break
            else:
                common.append(b[j:j+K])
                # i+=1 #?
                break
            
    return common

commons = check(mat[0],mat[1])
commons2 = []

flag = 0
if commons:
    flag = 1

for i in range(2,N):
    for com in commons:
        temp = check(com,mat[i]) 
        temp_r = check(com, list(reversed(mat[i])))
        commons2 += (temp + temp_r) 
    commons = commons2[:]
    commons2 = []
    if not commons:
        flag = 0
        break
if flag:
    print('YES')
else:
    print('NO')