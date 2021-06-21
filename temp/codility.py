# def solution(S, C):
#     company = C.lower()
#     people = S.split(';')
#     answer = ''
#     d = dict()
#     for person in people:
#         pars = person.strip().split()
#         f = pars[0].strip().lower()
#         l = pars[-1].lower().replace('-','')[:8]
#         name = ''.join([person.strip(),' '])
#         tmp = ''.join(['<',f,'.',l,'@',company,'.com>; '])
#         if d.get(tmp,0):
#             d[tmp]+=1
#             cnt = d[tmp]
#             tmp = tmp.replace('@',str(cnt)+'@')
#         else:
#             d[tmp] = 1
#         answer+= name+tmp
#     print(answer)
#     return answer.strip()

# solution()
# # solution('a','a')




# import datetime
# def solution(S):
#     # write your code in Python 3.6
    
#     files = S.split('\n')
#     max_size = 14*(2**20) # byte
#     last_date = datetime.date(1990,1,31)
#     size_d = {'M':2**20, 'K':2**10,'G':2**30}
#     mn = float('inf')
#     for f in files:
#         if f[-1] != '~':
#             continue
#         col = f.strip().split()
#         if size_d.get(col[0][-1],0):
#             tmp = size_d[col[0][-1]]*int(col[0][:-1])
#         else:
#             tmp = int(col[0])
#         if tmp >= max_size:
#             continue
#         if datetime.date(*map(int,col[1].split('-'))) <= last_date:
#             continue
#         dot = 0
#         for i in range(len(col[2])-1,-1,-1):
#             if col[2][i] == '.':
#                dot = i
#                break
#         if dot < mn:
#             mn = dot
#     return mn 

# solution(S)


R = [0]*10000000
mx = 0
def recursion(N, k, tmp, total):
    global mx, R
    if total == N:
        if k > mx:
            R = tmp[:k]
            mx= k
        return
    if tmp[k-1]%2:
        start = tmp[k-1]+2
    else:
        start = tmp[k-1]+1
    for i in range(start,N+1,2):
        if tmp[k] == 0 and total+i<=N:
            tmp[k] = i
            recursion(N,k+1,tmp,total+i)
            tmp[k] = 0 
def solution(N):

    recursion(N, 0, R, 0)
    return R[:mx]

print(solution(11))
# print(R[:10])