# 우선 1,11,111,1111,... 주변 숫자에 이것끼리 사칙연산은 확정
# 이전 거 더하기 1 or N, 이 숫자 이외는 어려울거 같은데...


def solution(N, number):
    INF = float('inf')
    # K = 32000*N+1
    K = 32000
    # 전체 배열
    a = [INF]*(32000*9+1)
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

            # if 0<x+1<K and a[x+1] > a[x] + a[1]:
            #     a[x+1] = a[x] +a[1]
            # if 0<x-1<K and a[x-1] > a[x] + a[1]:
            #     a[x-1] = a[x] +a[1]
            # if x+y == number:
            #     print(x,y,'+', a[x]+j+1)
            # if x*y == number:
            #     print(x,y,'x',a[x]+j+1)
            # if y-x == number:
            #     print(x,y,'-',a[x]+j+1)
            # if y//x == number:
            #     print(x,y,'//',a[x]+j+1)

            if x > y:
                x,y = y,x
            if 0<x+y<K and a[x+y] > a[temp]+a[k_list[j]]:
                a[x+y] = a[temp]+a[k_list[j]]
                queue.append(x+y)
            if 0<y-x<K and a[y-x] > a[temp]+a[k_list[j]]:
                a[y-x] = a[temp]+a[k_list[j]]
                queue.append(y-x)
            if 0<x*y<K and a[x*y] > a[temp]+a[k_list[j]]:
                a[x*y] = a[temp]+a[k_list[j]]
                queue.append(x*y)
            if 0<y//x<K and a[y//x] > a[temp]+a[k_list[j]]:
                a[y//x] = a[temp]+a[k_list[j]]
                queue.append(y//x)
    print(a[17])
    for i in range(10,K):
        
        a[i] = min(a[i], a[i-1]+a[1],a[i-2]+a[2],a[i-3]+a[3],a[i-4]+a[4],a[i-5]+a[5],a[i-6]+a[6],a[i-7]+a[7],a[i-8]+a[8],a[i-9]+a[9])

    print(a[:11])
    answer = a[number] 
    # if answer > 7: 
    #     answer = -1 
    return answer
# e= 5
# print('N = ',e)
# for i in range(1,21):
#     print( f'{i}는 {solution(e,i)}')
# print(solution(5,11))




            # if 0<temp+1<K and a[temp+1] > a[temp]+a[1]:
            #     a[temp+1] = a[temp] + a[1]
            # if 0<x-1<K and a[temp-1] > a[temp]+a[1]:
            #     a[temp-1] = a[temp] + a[1]

print(solution(4,17),4)