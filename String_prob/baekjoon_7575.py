import sys
sys.stdin = open('baekjoon_7575.txt') # 파일명으로 받을까?


N, K = map(int, input().split())
mat = [0]*N
for i in range(N):
    mi = input()
    mat[i] = list(map(int,input().split()))

# n<=100, M<=1000
def pi(arr):
    l = len(arr)
    i = 0
    if l%2:
        j = l//2+1
    else:
        j = l//2 # 실수되었던가?
    p = 0
    while i < l//2:
        if arr[i] == arr[j]:
            p+=1
        i+=1
        j+=1
    return p

def check(A,B):
    a=A;b=B
    if len(A) < len(B):
        a,b = B,A # 이걸 바꾸면, 뒤집었을때 문제가 생기네
    # a가 더 길게
    i = len(a)-K # 뒤에 K만큼 부터 시작하기 위해 initial값 변경
    j = 0
    c=0; k=[]; common = []
    while i >= K-len(b): # 최소 k까지는 봐야함 
        while j < len(b):
            if 0 <= i+j < len(a): 
                if a[i+j] == b[j]:
                    #check
                    c+=1
                    k.append(a[i+j]) 
                else: # 일치하지 않으면
                    if c and c>=K:
                        common.append(k) # 다 똑같으면 효율이 떨어짐
                        # i-= ( pi(k))
                        # print(k)
                    c = 0
                    k=[]
            j+=1 
            if not i+j < len(a):
                break
        if c and c>=K:
            common.append(k) # 예전이랑 코드가 똑같이 나오네
        c = 0
        k=[]
        # 일치하지 않았을 때와 j를 다 돌았을때 초기화가 되야함
        i-=1
        j=0
    return (common)
#### ed가 붙은 수동태는 list를 리턴해주지 않고 지들 명령어 객체를 돌려줘서 list한 번 더 써줌 ㅅㅂ, 원본이 훼손되지 않음, sort같은 친구들은 원본이 훼손되고 none을 리턴

# 2 <= N 이므로 처음 2개를 비교

commons = check(mat[0],mat[1])
commons2 = []

for i in range(2,N):
    for com in commons:
        temp = check(com,mat[i]) # 숫자가 다 같을 경우 매우 많이 나옴, pi가 존재하면, 바로 return값에 넣지 말아야함, 이게 반복 문자열의 경우, 경우의 수가 매우 많아짐, 부분 문자열 여부를 봐야하나? 다같은 경우는 pi를 이용하면 배제가 되나, 반복되는게 섞여 있는경우는?
        temp_r = check(com, list(reversed(mat[i])))
        commons2 += (temp + temp_r) 
    commons = commons2[:]
    commons2 = [] # 초기화를 안했네
    print(commons)
    if not commons:
        print('NO')
        break
else:
    print('YES')