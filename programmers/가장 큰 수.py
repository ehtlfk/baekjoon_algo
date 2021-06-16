# 앞자리가 같고 문자열의 길이가 다를 경우 짧은 쪽을 순환수라고 생각하면 된다.
# n = 10^5이므로 merge or heap or quick sort를 해야함
# len(numbers) > range(n) 이므로 중복되는 숫자가 반드시 존재
# [0,0,0,0] = > 0 
def check(a,b):
    # l = max(len(a),len(b))
    # if len(b) == 0:
    #     return -2
    # 문자열을 합쳐서 큰 거 return
    comb1 = a+b
    comb2 = b+a
    if comb1 > comb2:
        return -1
    elif comb1 == comb2:
        return 0
    else:
        return 1
    
    
    # 문자열을 순환시키면 됨
    
    # for k in range(l):
    #     if a[k%len(a)] > b[k%len(b)]:
    #         return -1
    #     elif a[k%len(a)] < b[k%len(b)]:
    #         return 1
    # return 0
        
def solution(numbers):
    answer = ''
    s_numbers = [ str(number) for number in numbers]
    heap = ['']*100001
    # 100001이 안된다고??? 왜 안돼지???, delete 연산에서 heap의 범위를 이용하지 않았음
    cur = 1
    for i in range(len(s_numbers)):
        heap[cur] = s_numbers[i]
        tmp = cur
        while tmp//2 > 0:
            if check(heap[tmp//2],heap[tmp])>0:
                heap[tmp//2], heap[tmp] = heap[tmp], heap[tmp//2]
            tmp//=2
        cur+=1
        
    root = 1
    cur-=1
    while cur > 0:
        answer+=heap[root]
        heap[root] = heap[cur]
        heap[cur] = ''
        cur-=1
        while root*2<100001 and heap[root]: # root가 heap 크기를 넘으면 끝이구나
            if check(heap[root*2],heap[root*2+1]) > 0:
                if check(heap[root],heap[root*2+1]) > 0:
                    heap[root*2+1],heap[root] = heap[root], heap[root*2+1]
                    root = root*2+1
                else:
                    break
            
            # 같을 수 있고, right child가 없을 수 있고, 작을 수도 잇음
            else:
                if check(heap[root], heap[root*2]) > 0:
                    heap[root],heap[root*2] = heap[root*2], heap[root]
                    root *= 2
                else:
                    break
            
        root = 1
    # print(heap[:len(numbers)+3])
 
    return str(int(answer))