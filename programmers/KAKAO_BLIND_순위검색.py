# sql의 쿼리문은 어떤 방식으로 실행이 될까?
# 문제를 봤을 때 가장 쉬운 방법은 지원자 한 명 한 명을 다 해보는 것이다
# 하지만 오래 걸린다
# 지원자를 기준으로 하는 것이 아닌 항목(2가지 씩이기 때문)을 기준으로 교집합을 계속 구하면 될 것이다.
# 교집합은 어떻게 빠르게 구하는가?
# 1. 미리 교집합의 개수를 다 구해놓는다 : 범용성이 별로
# 2. id를 부여해서 교집합을 구한다
# 3. 미리 정렬해서 binary search한다


# value와 인덱스를 가지고 정렬해서 가장 높은 숫자의 인덱스를 구하기
def solution(info, query):
    answer = []
    d = dict()
    points = [0]*len(info)
    info.sort(key=lambda x:int(x.split()[-1]),reverse=True)
    print(info)
    for i in range(len(info)):
        info_split = info[i].split()
        for col in info_split[:-1]:
            if d.get(col,0):
                d[col].add(i)
            else:
                d[col]=set([i])
        points[i] = int(info_split[-1])
    
    for q in query:
        q_split = q.split(' and ')
        food, point = q_split[3].split()
        cnt = 0
        tmp = { i for i in range(len(info))}
        if q_split[0] != '-':
            tmp = d[q_split[0]]
        if q_split[1] != '-':
            tmp = tmp&d[q_split[1]]
        if q_split[2] != '-':
            tmp = tmp&d[q_split[2]]
        if food != '-':
            tmp = tmp&d[food]

        for i in tmp: # query * info = 5억
            if points[i] >=int(point):
                cnt+=1
        answer.append(cnt)
    return answer