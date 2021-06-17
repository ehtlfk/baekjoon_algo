# A일 경우 무시할 수 있다, 예시의 'JAZ' 는 커서를 왼쪽으로 옮겨서 Z를 찾았다.
# 완탐을 할 경우 2^20
# python도 int val = 'a'-97 이 되나?
# 아 뒤로 가는게 더 빠를 수 있다!, 그리디로 제일 가까운 단어로 가면됨

def solution(name):
    answer = 0
    ori = ['A']*len(name)
    asc2 = { chr(i): i-65 if i < 78 else 91-i for i in range(65,91)}
    for ch in name:
        answer+=asc2[ch]
    # 좌우만 생각하면 됨
    m = 0
    ori[m] = name[m]
    while ''.join(ori) != name:
        r=m+1
        l=m-1
        while name[r%len(name)]==ori[r%len(name)]:
            r+=1
        while name[l%len(name)]==ori[l%len(name)]:
            l-=1
        
        if abs(r-m) > abs(m-l):
            answer+=abs(m-l)
            m = l
        elif abs(r-m) <= abs(m-l):
            answer+=abs(r-m)
            m = r

        ori[m] = name[m]
        print(r,l,''.join(ori),m)
    return answer


print(solution('BBABAAAB'))

# print(solution('AAABAAAAAB'))

# 핵심은 'A'까지의 거리가 더 짧은 곳으로 가면됨, 거리가 같은 경우는 오른쪽으로가든 왼쪽으로 가든 상관이 없음


#BBABAAAB
# 문제 조건에 정확히는 마지막 인덱스에서 오른쪽커서를 눌러도 첫번째 인덱스에 간다는 말이 없습니다. 그러므로 좀더 정확한 답은 11이라고 볼 수 있습니다. 