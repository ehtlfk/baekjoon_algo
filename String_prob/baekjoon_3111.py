import sys
sys.stdin = open('String_prob/baekjoon_3111.txt')

p = input()
o = input()

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
c= 0
k = 0
# k가 cnt 역할 수행
stack = ''

flag = 1
# 건너뛰기 위해 while문을 활용
while c < len(o):  
    if k == len(p):
        k = 0
        if flag == 1:
            o = stack + o[c:]
            c = -1
        else:
            o = o[:c+1] + stack
            c= 0
        stack = ''
        flag *= -1
        continue
    if o[c] == p[k]:
        k+=1
    else:
        # 이부분이 오래 걸릴 수 있음
        stack+=p[:k]
        stack+=o[c]
        k = 0
    
    c+=1*flag
print(stack + p[:k])


