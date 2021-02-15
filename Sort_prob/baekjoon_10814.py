import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input())
# split은 list를 리턴
# \n을 제거해주지 않으므로 rstrip을 쓰장
# 퀵 소트는 분할 정복을 활용함
# 퀵과 병합의 차이는 무엇인가? 
# 퀵은 피벗을 활용하여 배열을 두 파트로 나눔
# 분할 정복은 나눠진 각 파트마다 정렬을 시행
# 그냥 분할 정복 할란다.
users = [ input().rstrip().split() for _ in range(N)]

# 10만개 계속 복사
def dnc(arr):
    l =  len(arr)
    if l==1:
        return arr
    elif l==2:
        if int(arr[0][0]) > int(arr[1][0]):
            arr[0], arr[1] = arr[1], arr[0]
        return arr
        # 짝수 홀수 구분 안해도됨
    return conquer(dnc(arr[:(l//2+l%2)]), dnc(arr[(l//2+l%2):]))

def conquer(arr1, arr2):

    narr = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if int(arr1[i][0]) < int(arr2[j][0]):
            narr.append(arr1[i])
            i+=1
        elif int(arr1[i][0]) > int(arr2[j][0]):
            narr.append(arr2[j])
            j+=1
        else:
            # 여기에서 ij를 같이 빼면 안됨, i쪽에 같은 숫자가 여러개면 답이 다르게 됨 
            narr.append(arr1[i])
            i+=1
    while i<len(arr1):
        narr.append(arr1[i])
        i+=1
    while j <len(arr2):
        narr.append(arr2[j])
        j+=1
    return narr
            
        

users = dnc(users)
for user in users:    
    print(' '.join(user))

