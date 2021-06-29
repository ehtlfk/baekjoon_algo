# sql의 쿼리문은 어떤 방식으로 실행이 될까?
# 문제를 봤을 때 가장 쉬운 방법은 지원자 한 명 한 명을 다 해보는 것이다
# 하지만 오래 걸린다
# 지원자를 기준으로 하는 것이 아닌 항목(2가지 씩이기 때문)을 기준으로 교집합을 계속 구하면 될 것이다.
# 교집합은 어떻게 빠르게 구하는가?

def solution(info, query):
    answer = []
    # d = dict()
    d = [0]*len(info)
    for i in range(len(info)):
        info_split = info[i].split()
        d[i] = info_split
    d.sort(key=lambda x:int(x[4]),reverse=True)
    for q in query:
        q_split = q.split(' and ')
        food, point = q_split[3].split()
        cnt = 0
        for person in d:
            if int(person[4]) < int(point):
                break
            if (person[0] == q_split[0] or q_split[0] == '-') and (person[1] == q_split[1] or q_split[1] =='-')  and (person[2] == q_split[2] or q_split[2] =='-') and (person[3] == food or food == '-'):
                cnt+=1
        answer.append(cnt)
    return answer