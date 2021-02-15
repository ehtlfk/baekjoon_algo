import sys, os, math

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

def great(a1,s,n):
    if n == 1 or n == 2:
        return a1
    else:
        an = 1
        for i in range(s,n+1):
            an*=(((2**(i-2))+2)%1000000007)
            an%=1000000007
        return (an*a1)%1000000007

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

    

line_num=int(input())
divide = 1000000007
# 리턴 값이면 출력속도가 느림
for i in range(line_num):
    a=list(map(int,input().split(' ')))
    if a[0]==1:
        a1,i,j=a[1], a[2], a[3]
        if i>j:
            i,j = j,i
        gcdn = great(a1,3,i)
        print(gcdn)
    elif a[0]==2:
        a1,i,j=a[1], a[2], a[3]
        if i>j:
            i,j = j,i
        p=0
        while True:
            if a1%(2**(p+1)) == 0:
                p+=1
            else:
                break
        if j>2:
            print(j+p-1)
        else:
            print(p)
    elif a[0]==3:
        a1,i,j=a[1], a[2], a[3]
        if i>j:
            i,j = j,i
        ni = max(2,i)
        ai = great(a1,3,ni)
        aj = great(ai,ni+1,j+1)
        ans = ((aj//2**(j-1))-(ai//2**(ni-2)))
        if i == 1:
            ans+=1    
        print(ans)
    elif a[0]==4:
        a1,k=a[1], a[2]
        temp= great(a1,3,k)
        print(temp)