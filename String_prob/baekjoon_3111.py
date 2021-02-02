import sys
sys.stdin = open('String_prob/baekjoon_3111.txt')

from collections import deque

# p = deque(input())
# o = deque(input())

p = 'ac'
o = deque('a'*3 + 'c'*3)
# 이문제는 KMP를 쓰지 않더라도 30만 *25라 천만을 넘지않음, NM =10000000, 그러므로 잘 해주면되는데 문자열 복사가 넘 오래 걸림
# 링크드 리스트를 쓰면 빨리 될 거 같기는 한데, 구현이 너무 빡셈,
# 연결 부위가 찾는 문자열이 아님을 증명하면 될듯?
# return은 p를 o에서 모두 제거

def pi(s):
    l = len(s)
    pi_arr =[0]*l
    for i in range(1,l+1):
        hl =i//2
        j = 0
        p = 0
        if i%2: 
            k = hl + 1
        else:
            k = hl
        while k < i:
            if s[j] == s[k]:
                p+=1
                j+=1
            else:
                p = 0
            k+=1
        pi_arr[i-1] = p
    return pi_arr



# 스택 2개를 이용해서 구현, 스택1애 임시 스택2를 복사(주소값만 되는가?)
# 이문제는 앞뒤로 지우는 문제였다
# k가 cnt 역할 수행

stack_l = deque()
stack_r = deque()
# 1이면 left, -1이면 right
flag = 1

# 건너뛰기 위해 while문을 활용
# 정방향만 생각

# while o:
#     if flag ==1:
#         c=0
#     else:
#         c=-1
#     for k in range(1,len(p)):
#         if o[c] == p[k*flag]:
#             c+= 1*flag
#         else:
#             break
#     if c == len(p)-1 or  c == -len(p):
#         for _ in range(len(p)-1):
#             if flag ==1:
#                 o.popleft()
#             else:
#                 o.pop()
#         o = stack_l + o + stack_r
#         stack_l = deque()
#         stack_r = deque()
#         flag*=-1
#     else:
#         if flag == 1:
#             stack_l.append(o.popleft())
#         else:
#             stack_r.appendleft(o.pop())
# print(stack_l + stack_r)


def left(o,p):
    while o: 
    # 이게 너무 오래 걸리는거 같당
        c= 0

        for k in range(len(p)):
            if len(o)> c and o[c] == p[k]:
                c+=1
            else:
                break
        if c == len(p):
            for _ in range(len(p)):
                o.popleft()
            return 1
        else:
            stack_l.append(o.popleft())
    return 0


def right(o,p):
    while o:
        c= -1
        for k in range(len(p)-1,-1,-1):
            if len(o) >= abs(c) and o[c] == p[k]:
                # 아 길이가 안될 수도 있네
                c-=1
            else:
                break
        if c == -len(p)-1:
            for _ in range(len(p)):
                o.pop()
            return 1
        else:
            stack_r.appendleft(o.pop())
    return 0


stack_l = deque()
stack_r = deque()
l_cursor = 0
r_curosr = -1
while True:
    # stack_l에 값이 있으면 합쳤을때 key가 생기는지 검사, 이거는 keyword의 길이 -1만큼의 제곱만 수행하면 됨
    # if stack_l:
    #     for i in range(-len(p)+1,0):
    #         cnt = 0
    #         # 길이 필요
    #         for j in range(len(p)):
    #             if 0 <i+j < len(stack_l):
    #                 if stack_l[i+j] == p[cnt]:
    #                     cnt+=1
    #                 else:
    #                     break
    #             else:
    #                 if o[len(stack_l) - (i+j)] == p[cnt]:
    #                     cnt+=1
    #                 else:
    #                     break
    #         else: 
    #             if cnt == len(p):
    #                 for _ in range(abs(i)):
    #                     stack_l.pop()
    #                 for _ in range(len(p)-abs(i)):
    #                     o.popleft()
    #                 break      
    if left(o,p):
        # o.extendleft(list(stack_l)[-len(p)+1:])
        for _ in range(len(p)-1):
            if stack_l:
                o.appendleft(stack_l.pop())
            if stack_r:
                o.append(stack_r.popleft())
        # 이부분이 진짜 오래걸림
        # stack_l = deque()
        # if stack_r:
        if right(o,p):
            # o.extend(list(stack_r)[:len(p)-1]) 
            for _ in range(len(p)):
                if stack_l:
                    o.appendleft(stack_l.pop())
                if stack_r:
                    o.append(stack_r.popleft())
            # + 연산은 해악이다. 절대 하지말것!
            # 여기가 문제다
            # stack_r = deque()
            
        else:
            break
    else:
        break
stack_l.extend(stack_r) 
print(''.join(list(stack_l)))
