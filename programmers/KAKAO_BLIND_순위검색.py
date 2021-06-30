# sql의 쿼리문은 어떤 방식으로 실행이 될까?
# 문제를 봤을 때 가장 쉬운 방법은 지원자 한 명 한 명을 다 해보는 것이다
# 하지만 오래 걸린다
# 지원자를 기준으로 하는 것이 아닌 항목(2가지 씩이기 때문)을 기준으로 교집합을 계속 구하면 될 것이다.
# 교집합은 어떻게 빠르게 구하는가?
# 1. 미리 교집합의 개수를 다 구해놓는다 : 범용성이 별로
# 2. id를 부여해서 교집합을 구한다
# 3. 미리 정렬해서 binary search한다


# 2개의 문자열이 같은 지를 보는 것도 오래걸리므로 문자로 바꾸자
# value와 인덱스를 가지고 정렬해서 가장 높은 숫자의 인덱스를 구하기
def check(code,d):
    ret = []
    for key in d.keys():
        for k in range(len(key)):
            if code[k] == '*':
                continue
            if key[k] != code[k]:
                break
        else:
            ret.append(key)
    return ret
def solution(info, query):
    answer = []
    new_info = dict()
    d = {'cpp':'0','java':'1','python':'2','backend':'0','frontend':'1','junior':'0','senior':'1','pizza': '0', 'chicken':'1','-':'*'}
    for i in info:
        tmp = ''
        i_split = i.split()
        code = ''.join([d[i_split[0]],d[i_split[1]],d[i_split[2]],d[i_split[3]]])
        if new_info.get(code,0):
            new_info[code].append(int(i_split[4]))
        else:
            new_info[code] = [int(i_split[4])]
    for q in query:
        q_split = q.split(' and ')
        food, point = q_split[3].split()
        code = ''.join([d[q_split[0]],d[q_split[1]],d[q_split[2]],d[food]])
        point_info = dict()
        for key,val in new_info.items(): 
            point_info[key] = [v for v in val if v>=int(point)]
        
        ret = check(code,point_info)
        cnt = 0
        
        answer.append(len(ret))
    return answer