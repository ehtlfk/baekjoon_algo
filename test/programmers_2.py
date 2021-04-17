def solution(s):
    stack = []
    idx = [0]*501
    for i in range(len(s)-1): # 마지막괄호 때문임, 오래 걸린 이유, 문자열 파싱 때문, ','의 유무나, '{'를 체크하는데 시간을 너무 오래씀
        # 2자리 이상 숫자를 바꾸는 과정
        if s[i] == '}':
            cnt = -1
            plus = 0
            while stack[-1]!='{':
                d_cnt = 0
                tmp = 0
                while stack[-1].isdigit():
                    tmp = int(stack.pop())*(10**d_cnt) + tmp
                    d_cnt+=1
                plus+=tmp
                cnt+=1
                if stack[-1] == ',':
                    stack.pop()
            stack.pop()
            idx[cnt] = plus
        else:
            stack.append(s[i])
    answer = [idx[0]]
    for j in range(1,len(idx)):
        if idx[j]:
            answer.append(idx[j]-idx[j-1])
        else:
            break
    return answer
def solution3(s):
    idx = [0]*501
    i=1
    while i<len(s)-1:
        if s[i] == '{':
            cnt = 0
            tmp = 0
            number = 0
        elif s[i] == '}':
            tmp += number
            idx[cnt] = tmp
        elif s[i] == ',':
            tmp+= number
            number = 0
            cnt+=1
        else:
            number = number*10+int(s[i])
        i+=1
    answer = [idx[0]]
    for j in range(1,len(idx)):
        if idx[j]:
            answer.append(idx[j]-idx[j-1]) 
        else:
            break
    return answer
print(solution3("{{2},{1,2,3},{2,1},{1,2,3,4}}"))



# priority queue, queue에서 뺏다가 다시 추가하면, priority queue를 생각해보자
import heapq
def solution2(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >1:
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        if tmp1<K:
            n = tmp1 + 2*tmp2
            answer+=1
            heapq.heappush(scoville,n)
        else:
            break
    if scoville and scoville[-1]<K:
        answer = -1

    return answer