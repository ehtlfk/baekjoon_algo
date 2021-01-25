import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
mat = [0]*N
for i in range(N):
    mi = input()
    mat[i] = list(map(int,input().split()))

def check(A,B):
    a=A;b=B
    if len(A) < len(B):
        a,b = B,A # 이걸 바꾸면, 뒤집었을때 문제가 생기네
    # a가 더 길게
    i=0; c=0; k=[]; common = []
    while i < len(a)-K: # 최소 k까지는 봐야함
        for j in range(len(b)):
            if i+j < len(a): 
                if a[i+j] == b[j]:
                    #check
                    c+=1
                    k.append(a[i+j]) # 아 연속성을 안넣었다, 지금보니까 시작점도 바꿔줘야됨
                else: # 일치하지 않으면
                    if c and c>=K:
                        common.append(k) # 다 똑같으면 효율이 떨어짐 
                    c = 0
                    k=[]
        i+=1
    return (common)
#### ed가 붙은 수동태는 list를 리턴해주지 않고 지들 명령어 객체를 돌려줘서 list한 번 더 써줌 ㅅㅂ, 원본이 훼손되지 않음, sort같은 친구들은 원본이 훼손되고 none을 리턴
commons = [mat[0]]
commons2 = []
for i in range(1,N):
    for com in commons:
        temp = check(com,mat[i])
        print(temp)
        temp_r = check(com, list(reversed(mat[i])))
        print(temp_r)
        commons2 += (temp + temp_r) 
    commons = commons2[:]
    print(commons)
    if not commons:
        print('NO')
        break
else:
    print('YES')