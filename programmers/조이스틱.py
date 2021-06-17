# A일 경우 무시할 수 있다, 예시의 'JAZ' 는 커서를 왼쪽으로 옮겨서 Z를 찾았다.
# 완탐을 할 경우 2^20
# python도 int val = 'a'-97 이 되나?
# 아 뒤로 가는게 더 빠를 수 있다!, 그리디로 제일 가까운 단어로 가면됨
def left_or_right(name,ori,answer,m):
    tmp = ori[:]
    tmp[m] = name[m]
    if name == ''.join(tmp):
        print(answer)
        return
    else:
        r=m
        l=m
        while name[r]==tmp[r]:
            r+=1
        while name[l]==tmp[r]:
            l-=1
        print(l,r)
        if r<=abs(l):
            while name[r] != tmp[r]:
                tmp[r+1] = name[r]
                r+=1
            left_or_right(name,tmp,answer,r-1)
        else:
            left_or_right(name,tmp,answer,l)

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

print(solution('BBB'))

# 핵심은 'A'까지의 거리가 더 짧은 곳으로 가면됨, 거리가 같은 경우는 오른쪽으로가든 왼쪽으로 가든 상관이 없음