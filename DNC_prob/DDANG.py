import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

N = int(input()) #N = 2^M

dd = list(map(int,input().split()))

mx = 0
def divide(arr,total):
    global mx
    l = len(arr)//2

    if l == 1:
        total+=max(arr)
        if total > mx:
           mx = total
        return
    m1 = max(arr[:l])
    m2 = max(arr[l:])
    if m1 > m2:
        divide(arr[l:], total+m1)
    elif m2 > m1:
        divide(arr[:l], total+m2)
    else:
        divide(arr[:l], total+m1)
        divide(arr[l:], total+m1)
divide(dd,0)
print(mx)