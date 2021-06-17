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
    
    left_or_right(name,ori,answer,0)
    return answer
    # left_or_right(name,ori,0,answer,asc2)
    # 가장 긴 'A' sequence를 찾음
    # 원형으로 이어져서 'A'가 제일 길 수 있음 'AABBAAABBAA'
    # 전부 A인것도 못잡음
#     mx = 0
#     a_finish = 0
#     i = 0
#     while i < len(name):
#         tmp = 0
#         tmp_j = 0
#         for j in range(i,len(name)):
#             if name[j] =='A':
#                 tmp+=1
#                 tmp_j = j
#             else:
#                 break
#         i = j+1
#         if tmp >= mx:
#             mx = tmp
#             a_finish = tmp_j
#     if name[0] == 'A'and name[-1] == 'A' and mx!=len(name):
#         r=0
#         while name[r+1]=='A':
#             r+=1
#         l=0
#         while name[l-1]=='A':
#             l-=1
#         print(l,r)
#         if r<abs(l):
#             for i in range(len(name)+l):
#                 answer+=asc2[name[i]]+1
#             answer-=1
#         else:
#             for i in range(0,r-len(name),-1):
#                 answer+=asc2[name[i]]+1
#             answer-=1
        
#     elif mx:
#         r = max(a_finish-mx, 0) 
#         l = a_finish-len(name)+1
#         for i in range(len(name)):
#             answer+=asc2[name[i]]
        
#         answer+= 2*min(r,abs(l)) + max(r,abs(l))
#     else:
#         for ch in name:
#             answer+=asc2[ch]
#         answer+= len(name)-1
#     if ori == name:
#         answer = 0