import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

def great(a1,n,memo_num):
    if n == 1 or n == 2:
        return a1,memo_num
    else:
        if memo_num > n:
            return memo[n], memo_num
        else:
            an = memo[memo_num]
            for i in range(memo_num+1,n+1):
                an*=(2**(i-2))+2
                memo[i] = an
            memo_num = n
            return an*a1,memo_num

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

    

line_num=int(input())
memo = [1]*((10**6)+1)
memo_num = 2
# 리턴 값이면 출력속도가 느림
for i in range(line_num):
    a=list(map(int,input().split(' ')))
    if a[0]==1:
        [a1,i,j]=a[1:]
        if i>j:
            i,j = j,i
        gcdn,memo_num=great(a1,i,memo_num)
        print(gcdn%1000000007)
    elif a[0]==2:
        [a1,i,j]=a[1:]
        if i>j:
            i,j = j,i
        lcmn,memo_num=great(a1,j,memo_num)
        c=0;p=-1
        while c==0:
            p=p+1
            c=lcmn%2**p    
        print((p-1)%1000000007)
    elif a[0]==3:
        [a1,i,j]=a[1:]
        if i>j:
            i,j = j,i
        temp,memo_num = great(a1,i,memo_num)
        total = temp
        if i>1:
            for k in range(i+1,j+1):
                temp*=((2**(k-2))+2)
                total+=temp
        else:
            total = 2*a1
            for k in range(3,j+1):
                temp*=((2**(k-2))+2)
                total+=temp
        print(total%1000000007)
    elif a[0]==4:
        [a1,k]=a[1:]
        temp,memo_num = great(a1,k,memo_num)
        print(temp%1000000007)