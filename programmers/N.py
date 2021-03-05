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
    K = 32001
    # 전체 배열
    a = [INF]*(32001*9+1)
    k = N
    k_list = []
    cnt = 0
    while k < K:
        k_list.append(k)
        cnt+=1
        a[k] = cnt 
        k = 10*k+N
    queue = k_list[:]

    while queue:
        temp = queue.pop(0)
        for j in range(len(k_list)):
            x = temp
            y = k_list[j]
            if x > y:
                x,y = y,x
            if 0<x+y<K and a[x+y] > a[temp]+j+1:
                a[x+y] = a[temp]+j+1
                queue.append(x+y)
            if 0<y-x<K and a[y-x] > a[temp]+j+1:
                a[y-x] = a[temp]+j+1
                queue.append(y-x)
            if 0<x*y<K and a[x*y] > a[temp]+j+1:
                a[x*y] = a[temp]+j+1
                queue.append(x*y)
            if 0<y//x<K and a[y//x] > a[temp]+j+1:
                a[y//x] = a[temp]+j+1
                queue.append(y//x)
    answer = a[number] 
    if answer > 7: 
        answer = -1 
    return answer
# e= 5
# print('N = ',e)
# for i in range(1,21):
#     print( f'{i}는 {solution(e,i)}')
print(solution(1,1121))
