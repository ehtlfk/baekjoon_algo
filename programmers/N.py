# 우선 1,11,111,1111,... 주변 숫자에 이것끼리 사칙연산은 확정
# 이전 거 더하기 1 or N, 이 숫자 이외는 어려울거 같은데...

def recursion(N,number,a):
    if number > len(a) or number <= 0:
        return 320000
    if a[number]:
        return a[number]
    else:
        a[number] = min( recursion(N,number+N,a)+1,recursion(N,number-N,a)+1 )
    # if number == N:
    #     k=0
    #     while N >0:
    #         N//=10
    #         k+=1
    #     return k
    # elif number> 32000:
    #     return 12
    # if number%N == 0:
    #     return min(recursion(N,number-N), recursion(N,number+N)+1, recursion(N,number*N)+1, recursion(N,number//N)+1)
    # else:
    # return min(recursion(N,number-N)+1, recursion(N,number+N)+1, recursion(N,number*N)+1)
def solution(N, number):
    INF = float('inf')
    K = 32000*N+1
    # 전체 배열
    a = [INF]*(32001*9+1)
    k = N
    k_list = []

    if N !=1:
        a[1] = 2

    cnt = 0
    while k < K:
        k_list.append(k)
        cnt+=1
        a[k] = cnt 
        k = 10*k+N
    
    # for i in range(len(k_list)):
    #     for j in range(i+1,len(k_list)):
    #         x = k_list[i]
    #         y = k_list[j]
    #         if 0<x+y<K:
    #             if a[x+y] > i+j+2:
    #                 a[x+y] = i+j+2
    #         if 0<y-x<K:
    #             if a[y-x] > i+j+2:
    #                 a[y-x] = i+j+2
    #         if 0<x*y<K:
    #             if a[x*y] > i+j+2:
    #                 a[x*y] = i+j+2
    #         if 0<y//x<K:
    #             if a[y//x] > i+j+2:
    #                 a[y//x] = i+j+2
     
    for x in range(1,30):
        for y in range(1,30):
            if 0<x+y<K:
                if a[x+y] > a[x]+a[y]:
                    a[x+y] = a[x]+a[y]
            if 0<y-x<K:
                if a[y-x] > a[x]+a[y]:
                    a[y-x] = a[x]+a[y]
            if 0<x*y<K:
                if a[x*y] > a[x]+a[y]:
                    a[x*y] = a[x]+a[y]
            if 0<y//x<K:
                if a[y//x] > a[x]+a[y]:
                    a[y//x] =a[x]+a[y]

    for i in range(2,32001):
        if i%N == 0:
            a[i] = min ( a[abs(i-N)] + a[N],  a[i//N]+a[N], a[i], a[i-1]+a[1])
        else:
            a[i] = min ( a[abs(i-N)] + a[N], a[i], a[i-1]+a[1])
        if a[i//N] > a[i]+a[N]:  
            a[i//N] = a[i]+a[N]
        if a[i-N] > a[i]+a[N]:
            a[i-N] = a[i]+a[N]
        if a[i+N] > a[i]+a[N]: 
            a[i+N] = a[i]+a[N]
        if a[i*N] > a[i]+a[N]:
            a[i*N] = a[i]+a[N] 




    answer = a[number] 
    # if answer > 7: 
    #     answer = -1 
    return answer
e= 5
# print('N = ',e)
# for i in range(1,21):
#     print( f'{i}는 {solution(e,i)}')
print(solution(5,20))