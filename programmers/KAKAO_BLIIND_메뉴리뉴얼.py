# combinations를 비트로 구현하기
# 2개 요리로 된 코스의 경우의 수 : 모든 문자열에서 나올 수 있는 2가지의 문자
# 이걸 mapping하면 됨
from itertools import combinations

def make_course(n,order,d):
    combs = map(''.join,combinations(sorted(order),n))
    for comb in combs:
        if d.get(comb,0):
            d[comb]+=1
        else:
            d[comb] = 1
def solution(orders, course):
    answer = []
    
    for n in course:
        mx = 2
        tmp = []
        d = dict()
        for order in orders:
            make_course(n,order,d)
        
        for key, value in d.items():
            if value > mx:
                mx = value
                tmp = [key]
            elif value == mx:
                tmp.append(key)
        answer.extend(tmp)

    answer.sort()
    return answer