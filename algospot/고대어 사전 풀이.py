import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline


sub = ord('a')  
for _ in range(int(input())):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    alpha = [set() for _ in range(26) ]
    i=0
    while i<len(words)-1:
        k = 0
        while k<min(len(words[i]), len(words[i+1])):
            if words[i][k] == words[i+1][k]:
                k+=1
            else:
                alpha[ord(words[i][k])-sub].add(ord(words[i+1][k])-sub)
                break
        i+=1

# 생각해보니 철자가 중복될 수 있음

# 이 다음은 DAG인지 아닌지를 봐야됨
   
    t = []
    def dfs(node):
        v[node] =1
        for e in alpha[node]:
            if v[e] == 0:
                
                dfs(e)
              
        # if node not in t:
        t.append(node)
    v = [0]*26
    for i in range(25,-1,-1):
        # v를 초기화 시켜줘야됨
        if v[i] ==0:
            dfs(i)
    def checkDAG(arr):
        for i in range(len(arr)): # 이걸 len 으로 하니까 그렇지....
            for j in alpha[i]:
            # for j in range(i+1,len(arr)):
                if i in alpha[j]:
                    print(i,j)
                    return False
        return True
    ans = list(reversed(t))
    print(ans)
    if not checkDAG(ans):
        print('INVALID HYPOTHESIS')
    else:
        print(''.join(map(chr,[i+sub for i in ans]) ))


    # dfs, v 초기화 위치를 위로 해야 t.append를 할 때 중복 검사를 하지 않아도더;ㅁ
    # dag j 반복문에서 전체를 돌리면 안되는 이유? i 반복문을 숫자 순서대로 돌렸다. ...