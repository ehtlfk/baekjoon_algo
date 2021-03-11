import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

skill = input().split()
skill_dict = { i:idx for idx,i in enumerate(skill) }
N = int(input())
combo = [ [] for _ in range(len(skill))]

r = [0]*len(skill) # 데이터를 받을때 root를 체크하자

for _ in range(N):
    x,y = input().split()
    combo[skill_dict[x]].append(skill_dict[y])
    r[skill_dict[y]] =1

v = [0]*len(skill)

rr = []
a = [-1]*len(skill)
# 자식이 있는 친구들, root 후보
for j in range(len(skill)):
    if r[j] == 0:
        rr.append(j)
def dfs(p,k):
    a[k] = p
    if not combo[p]:
        a[k] = p
        print(  ' '.join([skill[em] for em in a if em!=-1 ]))
        a[k] = -1
        return
    else:
        for e in combo[p]:
            if v[e] == 0:
                v[e] = 1
                a[k+1] = e
                dfs(e,k+1)
                a[k+1] = -1
                v[e] = 0
for mr in rr:
    dfs(mr,0)

# 단방향 그래프 그리기
# root들을 찾음
# 조상을 찾음?