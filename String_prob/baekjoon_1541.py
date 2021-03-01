import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

f = input().strip()
ans = 0
i = 0
flag = 1
temp = ''
while i<len(f):
    if f[i] == '-':
        ans +=int(temp)*flag
        temp = ''
        flag = -1
    elif f[i] == '+':
        ans += int(temp)*flag
        temp = ''

    else: # 숫자
        temp+=f[i]
    i+=1
ans+= int(temp)*flag
print(ans)