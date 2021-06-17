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

for t in range(int(input())):
    solution(input())
print(solution('BBABAAAB'))

# print(solution('AAABAAAAAB'))

# 핵심은 'A'까지의 거리가 더 짧은 곳으로 가면됨, 거리가 같은 경우는 오른쪽으로가든 왼쪽으로 가든 상관이 없음


#BBABAAAB
 
# 백준 3663이 test case가 더 많음. 같은 코드로 제출했을 시 오답처리됨

# 참고(그리디가 아닌 이유) https://velog.io/@hsw0194/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
