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
def bs(lists,p):
    l = 0
    r = len(lists)-1
    while l<=r:
        m = (l+r)//2
        if lists[m] <p:
            r = m-1
        else:
            l = m+1
    return l
def perm(d,n,k,ret,v):
    if n == k:
        d[''.join(ret)] = []
    else:
        for i in range(len(v[k])):
            if v[k][i] == 0:
                v[k][i] = 1
                ret[k] = str(i)
                perm(d,n,k+1,ret,v)
                v[k][i] = 0
def check(code,query):
    
    for k in range(len(query)):
        if query[k] == '0':
            continue
        if query[k] != code[k]:
            return False
    else:
        return True

def solution(info, query):
    answer = []
    new_info = dict()
    all_query = dict()
    d = {'cpp':'1','java':'2','python':'3','backend':'2','frontend':'1','junior':'2','senior':'1','pizza': '2', 'chicken':'1','-':'0'}
    
    ret = [0]*4
    v = [[0]*3 for _ in range(4)]
    v[0].append(0)
    perm(all_query,4,0,ret,v)
    
    for i in info:
        i_split = i.split()
        code = ''.join([d[i_split[0]],d[i_split[1]],d[i_split[2]],d[i_split[3]]])
    
        for key in all_query.keys():
            if check(code,key):
                all_query[key].append(int(i_split[4]))
        for val in all_query.values():
            val.sort(reverse=True)
    for q in query:
        
        q_split = q.split(' and ')
        food, point = q_split[3].split()
        code = ''.join([d[q_split[0]],d[q_split[1]],d[q_split[2]],d[food]])
        
        answer.append(bs(all_query[code],int(point)))

    return answer