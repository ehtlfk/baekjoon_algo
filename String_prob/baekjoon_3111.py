# import sys
# sys.stdin = open('String_prob/baekjoon_3111.txt')

from collections import deque

# p = '#' + input()
# o = list(reversed(input()))
p = '#' + 'abc'
# o = list(reversed('abc'*1000))
o = deque('abc'*100000)

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
while o:
    if flag ==1:
        c=0
    else:
        c=-1
    for k in range(1,len(p)):
        if o[c] == p[k*flag]:
            c+= 1*flag
        else:
            break
    if c == len(p)-1 or  c == -len(p):
        for _ in range(len(p)-1):
            if flag ==1:
                o.popleft()
            else:
                o.pop()
        o = stack_l + o + stack_r
        stack_l = deque()
        stack_r = deque()
        flag*=-1
    else:
        if flag == 1:
            stack_l.append(o.popleft())
        else:
            stack_r.appendleft(o.pop())
print(stack_l + stack_r)



