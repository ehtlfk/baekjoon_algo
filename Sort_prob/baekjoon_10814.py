import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input())
# split은 list를 리턴
# \n을 제거해주지 않으므로 rstrip을 쓰장
# 퀵 소트는 분할 정복을 활용함
users = [ input().rstrip().split() for _ in range(N)]

# s_users = sorted(users, key= lambda x:x[0])
for i in range(len(users)-1):

    while i>=0: 
        if int(users[i][0]) > int(users[i+1][0]):
            users[i], users[i+1] = users[i+1], users[i]
            i-=1
        else:
            break
for user in users:    
    print(' '.join(user))

